N,M=map(int,input().split())
a=set([int(input()) for i in range(M)])
mod=10**9+7

if N==1:
  print(1)
  exit()

total=[0 for i in range(N+1)]
total[0] = 1
for i in range(1,N+1):
  if i>=2 and i-2 not in a:
  	total[i] += total[i-2]
  if i-1 not in a:
    total[i] += total[i-1]

print(total[-1] % mod)