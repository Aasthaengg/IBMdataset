n = int(input())
yt = 0
bt = 0
for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == 'JPY':
        yt += x
    else:
        bt += x

ans = yt + bt*380000
print(ans)