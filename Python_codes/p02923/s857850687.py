n=int(input())
h=list(map(int,input().split()))

d=[0]*(n-1)
k=0
if n==1:
  print(0)
  exit()
for i in range(n-1):
  if h[i]-h[i+1]>=0:
    d[k]+=1
  else:
    k+=1
print(max(d))