n,m,d = map(int, input().split())

ans = 0
num = max(0, n-d)*2
if d == 0:
    num //= 2
for _ in range(m-1):
    ans += num/n**2
print(ans)