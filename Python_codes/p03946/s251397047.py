n,t = map(int, input().split())
a = list(map(int, input().split()))
MAX = []
now = 0
for i in a[::-1]:
  now = max(i,now)
  MAX.append(now)
MAX.reverse()
max_margin = 0
ans = 0
for i,j in zip(a[:-1],MAX[1:]):
  margin = j-i
  if margin > max_margin:
    ans = 1
    max_margin = margin
  elif margin == max_margin:
    ans += 1
print(ans)