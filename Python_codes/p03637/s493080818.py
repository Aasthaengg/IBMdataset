n=int(input())
a=list(map(int,input().split()))
ans=[0]*3
for i in a:
  if i%4==0:ans[2]+=1
  elif i%2==0:ans[1]+=1
  else:ans[0]+=1
print(['No','Yes'][ans[0]+(ans[1]>0)<=ans[2]+1])