n = int(input())
x = 0
for i in range(n):
    a,b = input().split()
    if b == 'BTC':
        x += float(a)*380000
    else:
        x += int(a)
print(x)