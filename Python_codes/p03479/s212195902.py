x,y = map(int,input().split())
i=x
c=1
while i <= y:
  i*=2
  c+=1
print(c-1)