n=int(input())
li=list(map(int,input().split()))
lis=sorted(li)
dif=0
for (x,y)in zip(li,lis):
  if x!=y:
    dif+=1
if dif<3:
  print("YES")
else:
  print("NO")