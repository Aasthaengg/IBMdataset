n = int(input())
s = 0

for i in range(n):
    x,u = input().split()
    x = float(x)
    if(u == 'JPY'):s += x
    elif(u == 'BTC'):s += x * 380000
print(s)