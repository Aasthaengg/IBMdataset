N,M,Query = map(int,input().split())
from itertools import combinations_with_replacement
P = tuple(combinations_with_replacement(range(1,M+1),N))
Q = []
for _ in range(Query):
    a,b,c,d = map(int,input().split())
    Q.append((a,b,c,d))
    answer = 0
for p in P:
    ans = 0
    for a,b,c,d in Q:
        if p[b-1]-p[a-1]==c:
            ans += d
    answer = max(ans,answer)
print(answer)