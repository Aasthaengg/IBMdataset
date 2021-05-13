N=int(input())
d=list(map(int,input().split()))
ans = 0
from itertools import combinations
for i, j in combinations(range(N), 2):
    ans += d[i]*d[j]
print(ans)