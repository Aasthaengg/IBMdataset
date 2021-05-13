N = int(input())
S = list(input())
T = list(input())

ans = N + N
for i in range(N):
  w = S + T[-(i+1):]
  if w[:N] == S and w[-N:] == T:
    ans = min(ans,i+N+1)

if S == T:
  ans = N
    
print(ans)
    
