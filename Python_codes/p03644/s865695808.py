L = [2, 4, 8, 16, 32, 64]
n = int(input())

if n == 1:
  print(1)
  exit(0)

ans = 0
for l in L:
  if n < l:
    break
  ans = l

print(ans)