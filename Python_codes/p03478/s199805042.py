N,A,B=map(int,input().split())

SUM=0
for i in range(1,N+1):
  n = sum(map(int,list(str(i))))
  if A<=n and n<=B:
    SUM += i
print(SUM)