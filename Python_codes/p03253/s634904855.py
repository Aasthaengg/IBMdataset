n,m=map(int,input().split())
arr = []
q = 2
while q*q <= m:
  e = 0
  while m % q == 0:
    e += 1
    m //= q
  if e > 0: arr.append(e)
  q += 1
if m > 1: arr.append(1)
ans = 1
for e in arr:
  comb = 1
  for i in range(e):
    comb = comb * (n+i) // (1+i)
  ans = ans * comb % 1000000007
print(ans)