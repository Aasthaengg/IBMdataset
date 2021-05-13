from collections import Counter

n = int(input())
v = list(map(int, input().split()))

x = Counter(v[::2]).most_common(2)
y = Counter(v[1::2]).most_common(2)
ans = n
if x[0][0] == y[0][0]:
  if len(x) == len(y) == 1:
    ans = n//2
  else:
    s = max([a[1] for a in x]) + min([b[1] for b in y])
    t = min([a[1] for a in x]) + max([b[1] for b in y])
    ans -= max(s, t)
else:
  ans -= x[0][1] + y[0][1]
print(ans)