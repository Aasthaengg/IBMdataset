n,m=map(int,input().split())
sc=[]
for _ in range(m):
  s,c=map(int,input().split())
  sc.append([s,c])
for i in range(1000):
  j=list(str(i))
  if len(j)==n:
    for k in range(m):
      s,c=sc[k]
      if j[s-1]!=str(c):
          break
    else:
      print(i)
      exit()
print(-1)