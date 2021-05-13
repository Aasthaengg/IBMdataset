x,y=map(int,input().split())
ans=0
for n in range(x+1):
  if n*2+(x-n)*4==y:
    ans=1
    break
if ans==1:
  print('Yes')
else:
  print('No')