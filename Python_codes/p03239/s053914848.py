N,T=map(int,input().split())
ct=[0]*N
cost=[]
for i in range(N):
  ct[i]=list(map(int,input().split()))
  if ct[i][1]<=T :
    cost.append(ct[i][0])
if cost==[] :
  print("TLE")
else :
  print(min(cost))