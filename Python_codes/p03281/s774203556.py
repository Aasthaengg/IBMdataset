N = int(input())

if N < 105:
  ans = 0
elif N == 105:
  ans = 1
else:
  ans = 1
  for n in range(106, N+1):
    if n % 2 == 0:
      continue
    count = 0
    for i in range(1, int(n**(1/2))+1):
      if n % i == 0:
      	count += 1
    if count == 4:
      ans += 1
print(ans)
