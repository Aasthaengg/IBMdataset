N, K = map(int,input().split())
As = list(map(int, input().split()))
P = 10**9 + 7

memo = [0]*N
tmp = [0]*(2002)
sm = [0]*(2002)

for i in range(N):
  for j in range(As[i]+1,2001):
    memo[i] += tmp[j]
  tmp[As[i]] += 1
  
for i in range(2000, 0, -1):
  sm[i] += sm[i+1] + tmp[i]
  
rlt = 0

for i in range(N):
  rlt += (K*(K-1)*sm[As[i]+1]//2 + K*memo[i]) % P
  rlt %= P
  
print(rlt)