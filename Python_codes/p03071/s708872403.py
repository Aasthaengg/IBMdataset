a,b = map(int,input().split())
coin = 0
counter = 0

while counter < 2:
  if a >= b:
    coin += a
    a -= 1
  else:
    coin += b
    b -= 1
  counter += 1
print(coin)