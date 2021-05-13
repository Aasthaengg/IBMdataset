n = int(input())
nlen =len(str(n))
ans = 0
 
if n <= 9:
  print(n)
else:
  for i in range(1,nlen):
    if i % 2 == 1:
      ans += 10 ** i -10 ** (i-1)
  if nlen % 2 == 1:
    ans = ans + (n - 10**(nlen-1) + 1)
  print(ans)