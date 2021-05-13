N, P = map(int, input().split())
A = list(map(int, input().split()))
def comb(n, k):
  ret = 1
  for i in range(1, k+1):
    ret = ret * (n+1-i) // i
  return ret
Even = 0
Odd = 0
for a in A:
  if a % 2 == 0:
    Even += 1
  else:
    Odd += 1
ans = 0
while P <= Odd:
  ans += comb(Odd, P)
  P += 2
print(ans * 2 ** Even)