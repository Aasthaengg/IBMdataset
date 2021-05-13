x,y=map(int,input().split())
tmp=1
while True:
  x*=2
  if x>y:
    break
  else:
    tmp+=1
print(tmp)