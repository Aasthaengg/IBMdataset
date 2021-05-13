n=int(input())
a=[]
for i in range(n):
  b=int(input())
  c=[[] for _ in range(n)]
  for j in range(b):
    x,y=map(int,input().split())
    c[x-1]=y
  a.append(c)
ans=[]
for i in range(2**n):
  tr=bin(i)[2:].zfill(n)
  cnt=0
  for j in range(n):
    if tr[j]=='1':
      for k in range(n):
        if a[j][k]!=[] and a[j][k]!=int(tr[k]):
          break
      else:
        cnt+=1
  if sum(list(map(int,tr)))==cnt:ans.append(cnt)
print(max(ans))