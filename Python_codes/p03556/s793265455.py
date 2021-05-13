n = int(input())

ans = 0

for a in range(10**5 + 1):
    if a**2 <= n:
        ans = max(ans, a**2)

print(ans)
