from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
xy=[lnii() for i in range(n)]
xy.sort(key=lambda x:x[0])

pq=[]
for i in range(n-1):
  for j in range(i+1,n):
    t_p=xy[j][0]-xy[i][0]
    t_q=xy[j][1]-xy[i][1]
    pq.append([t_p,t_q])

ans=n
for p,q in pq:
  cnt=0
  for x,y in xy:
    if [x+p,y+q] in xy:
      cnt+=1
  '''
  for i in range(n):
    for j in range(n):
      if i==j:
        continue
      x1,y1=xy[i]
      x2,y2=xy[j]
      if (x2-x1)==p and (y2-y1)==q:
        cnt+=1
  '''

  ans=min(ans,n-cnt)
print(ans)