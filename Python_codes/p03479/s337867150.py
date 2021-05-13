x,y=map(int,input().split())
i=1
while True:
  x*=2
  if x>y:
    break
  i+=1
print(i)