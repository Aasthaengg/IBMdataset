N, K = list(map(lambda n: int(n), input().split(" ")))
 
while N > int(K/2):
  N = min([abs(N-K), N % K])

print(N)