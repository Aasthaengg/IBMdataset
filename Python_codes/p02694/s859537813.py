X=int(input())

y=1
m=100
while True:
  m += m//100
  if m>=X:
    print(y)
    exit(0)
  y+=1