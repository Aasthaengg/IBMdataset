from collections import Counter
N=int(input())
xy=[list(map(int,input().split())) for _ in range(N)]
xy.sort()

if N==1:
  print(1)
  exit()

pq=[]
for i in range(N):
  for j in range(i+1,N):
    pq.append([xy[j][0]-xy[i][0],xy[j][1]-xy[i][1]])

print(N-Counter(map(lambda x:x[0]*10**10+x[1],pq)).most_common()[0][1])