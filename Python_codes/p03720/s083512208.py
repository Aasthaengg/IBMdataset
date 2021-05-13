N,M=map(int,input().split())
l=list()
for i in range(M):
  a,b=map(int,input().split())
  l.append(a)
  l.append(b)
for n in range(1,N+1):
  print(l.count(n))