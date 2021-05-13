n = int(input())
ans = 0
if n <= 2:
  ans = 1%n
else:
  ans = n*(n-1)//2
print(ans)