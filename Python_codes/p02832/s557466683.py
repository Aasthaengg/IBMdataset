n=int(input())
a=list(map(int,input().split()))
data=[]
k=0
for i in range(n):
  if a[i]==k+1:
    data.append(a[i])
    k+=1
if len(data)!=0:
  print(n-len(data))
else:
  print(-1)