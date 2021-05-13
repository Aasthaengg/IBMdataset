n,k = map(int,input().split())
ans = 0

if k == 0:
    print(n**2)
    exit()

for b in range(k+1, n+1):
    x = n // b
    y = n % b
    ans += (b - k) * x + max(0, y - k + 1)

print(ans)
