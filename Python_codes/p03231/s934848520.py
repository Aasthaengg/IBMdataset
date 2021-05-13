import fractions

N,M = map(int,input().split())
S = input()
T = input()
L = fractions.gcd(N,M)
ans = N*M//L

if L == 1:
  print(ans) if S[0] == T[0] else print(-1)
else:
  print(ans) if S[::N//L] == T[::M//L] else print(-1)