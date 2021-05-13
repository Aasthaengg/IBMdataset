n = int(input())
sum = 0
for i in range(0,n):
    x,u = input().split()
    x = float(x)
    if u == 'BTC':
        x = x *380000
    sum = sum + x
print (sum)