n,k=map(int,input().split())
if k>((n-1)*(n-2))//2:
  print(-1)
  exit()
print(n-1+((n-1)*(n-2))//2-k)
for i in range(2,n+1):
  print(1,i)
cnt=((n-1)*(n-2))//2-k
for i in range(2,n+1):
  for j in range(i+1,n+1):
    if cnt>0:
      print(i,j)
      cnt-=1
    else:
      break