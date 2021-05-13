N = int(input())
A = list(map(int,input().split()))
Q = int(input())
BC = [tuple(map(int,input().split())) for i in range(Q)]
from collections import Counter
ctr = Counter(A)
sm = sum(A)

ans = []
for b,c in BC:
    n = ctr[b]
    sm -= n * b
    sm += n * c
    ctr[b] -= n
    ctr[c] += n
    ans.append(sm)
print(*ans, sep='\n')