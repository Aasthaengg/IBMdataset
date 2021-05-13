n = int(input())
a = list(map(int, input().split()))
ans = 0
if 1 not in a:
  ans = -1
else:
  k = 1
  for i in range(n):
    if a[i] == k:
      k += 1
    else:
      ans += 1
print(ans)