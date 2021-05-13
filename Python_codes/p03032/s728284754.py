n, k = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(1, min(n, k) + 1):
  for j in range(i + 1):
    l_tmp = l[:j] + l[n - i + j:]
    l_tmp.sort()
    for m in range(min(k - i, i)):
      if l_tmp[m] < 0:
        l_tmp[m] = 0
    ans = max(ans, sum(l_tmp))
print(ans)