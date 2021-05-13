import sys
input = sys.stdin.readline
N, Y = map(int, input().strip("\n").split())
for x in range(N + 1):
    for y in range(N - x + 1):
        remainder = Y - 10000 * x - 5000 * y
        if (N - x - y) * 1000 == remainder:
            print(" ".join([str(x), str(y), str(N - x - y)]))
            exit(0)
print("-1 -1 -1")