N, A, B = map(int,input().split())

sum = 0
for n in range(1,N + 1):
  d5, mod = divmod(n,10**4)
  d4, mod = divmod(mod,10**3)
  d3, mod = divmod(mod,10**2)
  d2, mod = divmod(mod,10)
  d1 = mod
  s = d1 + d2 + d3 + d4 + d5
  if A <= s <= B:
    sum += n

print(sum)