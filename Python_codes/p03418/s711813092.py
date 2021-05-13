N, K = map(int,input().split())

if K == 0:
  print(N*N)
  exit()

result = 0
for i in range(K+1, N+1):
  loop = int(N/i)
  result += (i-K)*loop
  result += max(N-K-(loop*i)+1,0)

print(result)
