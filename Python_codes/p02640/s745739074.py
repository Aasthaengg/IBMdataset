x,y=[int(i) for i in input().split()]
ans=0
for turu in range(x+1):
  kame=x-turu
  if turu*2+kame*4==y:
    ans=1
if ans==1:
  print("Yes")
else:
  print("No")