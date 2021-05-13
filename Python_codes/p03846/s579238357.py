N = int(input())
A = sorted([int(x) for x in input().split()])

flg = True
if N%2 == 0:
  for i in range(0, N//2): flg &= A[2*i] == A[2*i+1] == 2*i+1
else:
  flg &= A[0] == 0
  for i in range(1, (N+1)//2): flg &= A[2*i-1] == A[2*i] == 2*i

def modpow(n, r, m):
  if r == 0: return 1
  if r%2 == 0: return modpow(n, r//2, m)**2 % m
  return n * modpow(n, r-1, m) % m

print(modpow(2, N//2, 10**9+7) if flg else 0)
