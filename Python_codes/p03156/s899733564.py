N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
count=[0]*3
for i in range(N):
  if P[i]<=A :
    count[0]+=1
  elif P[i]<=B :
    count[1]+=1
  else :
    count[2]+=1
print(min(count))