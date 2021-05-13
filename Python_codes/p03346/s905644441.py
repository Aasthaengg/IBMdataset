N = int(input())
P = [0]
for i in range(N):
  P.append(int(input()))
Q = [0]*(N+1)
for i in range(1,N+1):
  Q[P[i]] = i
res = Q[1]
cnt = 0  
c = 1
for i in range(2,N+1):
  if res < Q[i]:
    c += 1
    res = Q[i]
    if i == N:
      cnt = max(cnt,c)
  else:
    cnt = max(cnt,c)
    c = 1
    res = Q[i]
ans = N-cnt
if N ==1:
  ans = 0    
print(ans)      