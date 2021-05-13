N, K = list(map(int, input().split()))
Pd = 1 / N
Pc = 0.5
ans = []
def f(i):
  P = Pd
  while(i<K):
    P = P * Pc
    i = 2 * i
  return P

for j in range(1,N+1):
  ans.append(f(j))
  
print(sum(ans))