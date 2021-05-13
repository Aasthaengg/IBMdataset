n,k,q=map(int,input().split())
p=[q]*(n+1)

for i in range(q):
  a=int(input())
  p[a]-=1
  
for i in range(1,n+1):
  if p[i]<k:
    print("Yes")
  else:
    print("No")