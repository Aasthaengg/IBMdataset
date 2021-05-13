n=int(input())
T=list(map(int,input().split()))
m=int(input())
nom=0
for i in range(n):
  nom+=T[i]
for i in range(m):
  p,x=map(int,input().split())
  ans=nom-T[p-1]+x
  print(ans)