N = int(input())

ans = 0
for a in range(1, N + 1):
    y = N // a
    ans += (y * (y + 1) * a) // 2
print(ans)
