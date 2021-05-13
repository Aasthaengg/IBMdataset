N = int(input())
As = [0]+list(map(int, input().split()))

memo = [0]*(N+1)

for i in range(N,0,-1):
  j = 2
  cnt = 0
  while i*j <= N:
    cnt ^= memo[i*j]
    j += 1
  memo[i] = cnt^As[i]
  
print(sum(memo))
rlt = []
for i in range(1,N+1):
  if memo[i] == 1:
    rlt.append(i)
    
print(' '.join(map(str, rlt)))