X,Y=map(int,input().split())

s=1

while X*2<=Y:
  X=X*2
  s=s+1
  
print(s)