N, M = map(int, input().split())

def diviser(n):
  i = 1
  ret = []
  while i * i <= n:
    if n % i == 0:
      ret.append(i)
      if n // i != i:
        ret.append(n // i)
    i += 1
  return ret

ans = 0
for i in sorted(diviser(M)):
  if i * N <= M:
    ans = max(ans, i)

print(ans)