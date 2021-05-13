n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
ans=[]
for i in range(8):
  binstr=format(i,"b").zfill(3)
  b=[]
  for j in range(n):
    c=0
    for k in range(3):
      if binstr[k]=="1":
        c+=a[j][k]
      else:
        c+=-a[j][k]
    b.append(c)
  b.sort(reverse=True)
  ans.append(sum(b[:m]))
print(max(ans))