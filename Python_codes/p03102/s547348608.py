N,M,C = map(int,input().split())
B = list(map(int,input().split()))
ans = 0

for n in range(N):
  P = 0
  A = list(map(int,input().split()))
  for a,b in zip(A,B):
    P += a*b
  if P+C>0:
    ans+=1
    
print(ans)