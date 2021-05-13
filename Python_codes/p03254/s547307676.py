N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0
j = 0
for i in range(N):
  if (cnt + a[i]) > x:
    break
  cnt += a[i]
  j += 1
if j == len(a):
  if x != cnt:
    j -= 1
print(j)