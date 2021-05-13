a,b = map(int,input().split())
coin = 0
if a >= b:
    coin += a
    a -= 1
else:
    coin += b
    b -= 1
if a >= b:
    coin += a
    a -= 1
else:
    coin += b
    b -= 1
print(coin)