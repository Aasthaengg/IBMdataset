n,m = map(int, input().split())
c = set(i+1 for i in range(m))
for j in range(n):
  l = list(map(int, input().split()))
  l.remove(l[0])
  c = c&set(l)
print(len(c))