import sys
N, M = [int(i) for i in sys.stdin.readline().split()]
v = [0] * N
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    v[a - 1] ^= 1
    v[b - 1] ^= 1
print("NO" if 1 in v else "YES")