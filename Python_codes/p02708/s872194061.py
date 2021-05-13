N, K = map(int, input().split())
answer = 0
MOD = 10**9+7
for i in range(K, N+2):
  lower = i*(i-1)//2
  upper = (N*(N+1)-(N-i)*(N-i+1))//2
  answer += (upper-lower+1)%MOD
print(answer%MOD)