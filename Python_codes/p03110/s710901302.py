n = int(input())
res = 0
for i in range(n):
    x, u = input().split()
    if u == 'JPY':
        res += float(x)
    elif u == 'BTC':
        res += float(x) * 380000.0
print(res)