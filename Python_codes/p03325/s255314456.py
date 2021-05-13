N = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(N):
  j = 0
  while 1:
    if a[i] % (2 ** (j + 1)) == 0:
      j += 1
    else:
      ans += j
      j = 0
      break
else:
  print(ans)