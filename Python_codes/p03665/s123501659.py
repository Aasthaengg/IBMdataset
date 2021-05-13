N, P = map(int, input().split())
A = list(map(int, input().split()))
def comb(x, y):
  m = c = 1
  for i in range(y):
    m *= x-i
    c *= y-i
  return m//c
even = odd = 0
for a in A:
  if a%2 == 0:
    even += 1
  else:
    odd += 1
ans = 0
for i in range(P, odd+1, 2):
  ans += comb(odd, i)
print(pow(2, even) * ans)
