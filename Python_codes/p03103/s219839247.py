import sys

N, M = map(int, sys.stdin.readline().split())

shops = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    shops.append((a, b))

ans = 0
num = 0
for a, b in sorted(shops):
    if num < M:
        if num + b < M:
            num += b
            ans += a * b
        else:
            ans += a * (M - num)
            break

print(ans)