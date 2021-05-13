n, x = map(int, input().split())
M = [int(input()) for _ in range(n)]

ans = 0
for m in M:
    ans += 1
    x -= m
ans += x // min(M)
print(ans)