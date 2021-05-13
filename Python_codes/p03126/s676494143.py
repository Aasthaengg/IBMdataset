n, m = map(int, input().split())
f = [i for i in range(1, m + 1)]
for i in range(n):
  a = list(map(int, input().split()))
  k = a[0]
  a = a[1:]
  f = set(f) & set(a)
f = list(f)
print(len(f))