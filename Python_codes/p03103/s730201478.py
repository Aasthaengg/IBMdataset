N,M=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(N)]
ab = sorted(ab)

SUM=0
for i in range(N):
  a,b=ab[i]
  x = min(M,b)
  SUM += a*x
  M -= x
  if M==0:break
    
print(SUM)