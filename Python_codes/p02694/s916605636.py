x=int(input())
m=100
for i in range(4000):
  m=int((m*101)//100)
  if m>=x:
    print(i+1)
    exit()