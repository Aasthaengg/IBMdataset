n,q=map(int,input().split())
s=input()
lr=[list(map(int,input().split())) for i in range(q)]
data=[0]*(n+1)
if s[0]=='A' and s[1]=='C':
  data[1]=1
for i in range(1,n-1):
  if s[i]=='A' and s[i+1]=='C':
    data[i+1]+=1
  data[i+1]+=data[i]
data[n]=data[n-1]
for i in range(q):
  print(data[lr[i][1]-1]-data[lr[i][0]-1])