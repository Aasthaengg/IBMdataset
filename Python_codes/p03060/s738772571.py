import sys

N = int(sys.stdin.readline())
V = list(map(int, sys.stdin.readline().strip().split()))
C = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
for i in range(N):
    tmp = V[i] - C[i]
    if tmp > 0:
        ans += tmp
print(ans)