X,Y=map(int,input().split())
total=1
while 1:
  X=X*2
  if X>Y:
    break
  total=total+1
print(str(total))