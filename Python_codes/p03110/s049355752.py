n = int(input())
total = 0
for i in range(n):
    x, u = map(str, input().split())
    x = float(x)
    if u == 'BTC':
        x *= 380000
    total += x
print(total)