n, t = map(int, input().split())
li = list(map(int, input().split()))
li = li[::-1]
ans = 0

for i in range(n):
  if i == 0:
    ans += t
  if i >= 1:
    if li[i-1]-li[i] >= t:
      ans += t
    else:
      ans += li[i-1]-li[i]
print(ans)