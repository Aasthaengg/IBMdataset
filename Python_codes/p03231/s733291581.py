import fractions
 
N, M = map(int, input().split())
S = input()
T = input()

cfac = fractions.gcd(N,M)

B = N//cfac
C = M//cfac
 
i = 0
for i in range(cfac):
  if S[i*B] != T[i*C]:
    print(-1)
    exit()
    
print(cfac*B*C)