n=int(input())
p=[]
for i in range(n):
  p.append(list(map(int,input().split())))
p.sort()

c=[set() for i in range(n)]
for i in range(n):
  for j in range(n):
    c[i].add((p[i][0]-p[j][0],p[i][1]-p[j][1]))
mn=1 if n==1 else 100
for i in range(n):
  for j in range(i+1,n):
    cnt=0
    pq=(p[i][0]-p[j][0],p[i][1]-p[j][1])
    for k in range(n):
      if not(pq in c[k]):
        cnt+=1
    mn=min(mn,cnt)
print(mn)
