import sys

N, M = map(int, input().split())
AB = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

AB.sort()

res = 0
for a, b in AB:
    if M > b:
        M -= b
        res += a * b
    else:
        res += a * M
        break
print(res)
