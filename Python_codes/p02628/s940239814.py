n, k = map(int, input().split())
p = [int(x) for x in input().split()]
a = [0]*k
for i in range(k):
  a[i] = min(p) + a[i-1]
  b = p.index(min(p))
  p[b] = 1001
print(a[k-1])