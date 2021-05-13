n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]
xy.sort()

pq=[]
for i in range(n-1):
  for j in range(i+1,n):
    pq.append([xy[j][0]-xy[i][0],xy[j][1]-xy[i][1]])

cnt=0
for p,q in pq:
  t_cnt=0
  for x,y in xy:
    if [x+p,y+q] in xy:
      t_cnt+=1
  cnt=max(cnt,t_cnt)

print(n-cnt)