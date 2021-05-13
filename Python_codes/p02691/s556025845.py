n = int(input())
a = list(map(int, input().split(' ')))
b = [a[i] + i for i in range(n)]
c = [j - a[j] for j in range(n)]
d = dict()
ans = 0
for i in range(n):
  if d.get(b[i]) is None:
    d.setdefault(b[i],1)
  else:
    d[b[i]] += 1
  if d.get(c[i]) is not None:
    ans += d[c[i]]
print(ans)