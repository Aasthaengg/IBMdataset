h,w=map(int,input().split())
ans=[]
for i in range(h):
  temp=list(map(str,input()))
  ans.append(temp)
  ans.append(temp)
for i in range(h*2):
  print("".join(ans[i]))