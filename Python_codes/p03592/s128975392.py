import sys
stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M, K = rl()

bool = [False] * (N * M + 1)
for i in range(N+1):
    bool[i*M] = True
    for j in range(1, M+1):
        x = N - (2 * i)
        if 0 <= i*M + x*j <= N * M:
            bool[i*M + x*j] = True

print('Yes' if bool[K] else 'No')
# 47