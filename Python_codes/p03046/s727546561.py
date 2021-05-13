import sys

M, K = map(int, sys.stdin.readline().strip().split())

if M == 1:
    if K == 0:
        print("0 0 1 1")
    else:
        print(-1)
else:
    if K >= 2**M:
        print(-1)
    else:
        a = [i for i in range(2**M) if i != K]
        b = sorted(a, reverse=True)
        print(" ".join(list(map(str, a + [K] + b + [K]))))