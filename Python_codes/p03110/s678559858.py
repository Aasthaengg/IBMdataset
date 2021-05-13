# B - Digital Gifts

N = int(input())
ans = 0
xrate = 380000

for i in range(N):
    x, u = map(str, input().split())
    if u == 'BTC':
        ans += float(x) * xrate
    else:
        ans += float(x)

print(ans)
