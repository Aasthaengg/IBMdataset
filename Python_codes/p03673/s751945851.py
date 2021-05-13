n = int(input())
a = list(map(int, input().split()))
r = []
l = []
for i in range(n):
  if i % 2 == 0:
    r.append(a[i])
  else:
    l.append(a[i])

if n % 2 == 0:
  ans = l[::-1]+r
else:
  ans = r[::-1]+l
print(" ".join(map(str, ans)))
