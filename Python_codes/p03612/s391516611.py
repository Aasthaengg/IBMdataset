N = int(input())
P = list(map(int,input().split()))

ans = 0
if P[-1] == N:
  P[-1],P[-2] = P[-2],P[-1]
  ans += 1

for i in range(N-1):
  if P[i] == (i+1):
    P[i],P[i+1] = P[i+1],P[i]
    ans += 1
    
print(ans)