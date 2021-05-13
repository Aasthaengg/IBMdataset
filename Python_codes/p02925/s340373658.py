N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
wait=[[float("inf")]*N for _ in range(N)]
for i in range(N):
  wait[A[i][0]-1][i]=0
L=[list(range(N)),[]]
finish=[0]*N

day=0
ind=0
while L[ind]:
  battle=False
  day+=1
  for player in L[ind]:
    if finish[player]>=N-1:
      continue
    enemy=A[player][finish[player]]-1
    if wait[player][enemy]<day and wait[enemy][player]<day:
      battle=True
      #print("day{},{}vs{}".format(day,player+1,enemy+1))
      finish[player]+=1
      finish[enemy]+=1
      if finish[player]<N-1:
        wait[A[player][finish[player]]-1][player]=day
      if finish[enemy]<N-1:
        wait[A[enemy][finish[enemy]]-1][enemy]=day
      L[(ind+1)%2].append(player)
      L[(ind+1)%2].append(enemy)
  L[ind]=[]   
  ind=(ind+1)%2
  if not battle:
    day-=1
    break
if min(finish)<N-1:
  print(-1)
else:
  print(day)
       
      
  


