n,k=map(int,input().split())
if k>((n-1)*(n-2))//2:
  print(-1)
else:
  print(n-1+((n-1)*(n-2))//2-k)
  for i in range(n-1):
    print(i+1)
    print(n)
  j=1
  l=2
  for i in range(((n-1)*(n-2))//2-k):
    print(j)
    print(l)
    l+=1
    if l==n:
      j+=1
      l=j+1

