import itertools
from sys import exit

N, K = map(int, input().split())
max_edge = (N - 1) * (N - 2) // 2
if K > max_edge:
    print(-1)
    exit()

print(N - 1 + max_edge - K)
for i in range(1, N):
    print(i, N)

cnt = max_edge
it = itertools.combinations(range(1, N), 2)
while cnt > K:
    print(*next(it))
    cnt -= 1
