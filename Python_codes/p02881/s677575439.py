n = int(input())

i = 1
ans = n-1
while i*i <= n:
  if n % i == 0:
    ans = min(ans, i-1 + n//i-1)
  i += 1

print(ans)