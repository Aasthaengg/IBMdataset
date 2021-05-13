i = int(input())
total = 0
for n in range(1,i+1,2):
  ans = 0
  for m in range(1,n+1):
    if n % m == 0:
      ans += 1
  if ans == 8:
    total += 1
print(total)