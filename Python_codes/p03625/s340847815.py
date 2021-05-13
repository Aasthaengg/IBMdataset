n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
s = set()
s.add(0)
s.add(-1)
for i in range(n-1):
  if a[i] == a[i+1]:
    s.add(a[i])
m = max(s)
s.discard(m)
k = max(s)
if a.count(m) > 3:
  print(m**2)
else:
  print(m*k)