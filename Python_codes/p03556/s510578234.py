n = int(input())
i = 1
while True:
  if i**2 > n:
    ans = (i-1)**2
    break
  i += 1
print(ans)