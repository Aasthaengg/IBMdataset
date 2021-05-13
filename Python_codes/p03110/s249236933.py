n = int(input())

ans = 0
for _ in range(n):
    x, u = input().split()
    if u == 'JPY':
        ans += int(x)
    else:
        ind = x.index('.')
        ans += int(x[:ind]) * 380000
        ans += int(x[ind+1:]) * 38 / 10000

print(ans)