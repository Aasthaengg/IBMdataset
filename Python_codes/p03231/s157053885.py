import fractions
  
def lcm(a,b):
  return (a * b) // fractions.gcd(a, b)

N,M = map(int,input().split())
S = input()
T = input()

if M > N:
  N,M = M,N
  S,T = T,S

X = lcm(N,M)

n = N // fractions.gcd(N,M)
m = M // fractions.gcd(N,M)

for i in range(0,X,m):
  if S[0] != T[0]:
    print(-1)
    break
  elif i % n == 0:
    s = i // n
    t = i // m
    if S[t] != T[s]:
      print(-1)
      break
else:
  print(X)
