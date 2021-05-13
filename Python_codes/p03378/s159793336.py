n,m,x=map(int,input().split())
a=[int(x) for x in input().split()]
cnt=0
for i in a:
  if i<x:
    cnt+=1
  else:
    break
cnt=min(cnt,m-cnt)
print(cnt)
