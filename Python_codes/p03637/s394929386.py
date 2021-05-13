n=int(input())
a=list(map(int,input().split()))
ans=[0]*3
for i in a:
  if i%4==0:
    ans[2]+=1
  elif i%2==0:
    ans[1]+=1
  else:ans[0]+=1
if ans[0]<=ans[2] or (ans[0]<=ans[2]+1 and ans[1]==0):print('Yes')
else:print('No')