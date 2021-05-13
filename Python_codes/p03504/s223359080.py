N,C=map(int,input().split())
TV=[[0]*C for i in range(10**5)]
for i in range(N):
  s,t,c=map(int,input().split())
  for i in range(s-1,t):
    TV[i][c-1]=1
print(max([sum(TV[i]) for i in range(10**5)]))