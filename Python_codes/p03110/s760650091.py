n = int(input())
jpy = 0
btc = 0
for i in range(n):
    x, u = map(str, input().split())
    if u == 'JPY':
        x = int(x)
        jpy += x
    else:
        x = float(x)
        btc += x
print(jpy + btc*380000.0)