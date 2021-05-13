import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A = map(int, read().split())

if N == 0:
    x = A[0]
    if x == 1:
        print(1)
    else:
        print(-1)
    exit()

INF = 10 ** 13 + 100

bound = [0] * (N + 1)
bound[0] = 1
ok = True
for n in range(1, N + 1):
    bound[n] = min(INF, (bound[n - 1] - A[n - 1]) * 2)
    if bound[n] < A[n]:
        ok = False

if not ok:
    print(-1)
    exit()

B = [0] * (N + 2)
for n in range(N, -1, -1):
    x = min(bound[n], B[n + 1] + A[n])
    B[n] = x

print(sum(B))

