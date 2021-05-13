n = int(input())
i, a, b = 2, 2, 1
ans = 0
if n==1:
  print(1)
  quit()
while i <= n:
  ans = a + b
  a,b = b, ans
  i += 1
print(ans)