n = int(input())

ans = 0
for div in range(1, int(n ** 0.5) + 1):
    if (n - div) % div == 0 and div < (n - div) // div:
        ans += (n - div) // div

print(ans)
