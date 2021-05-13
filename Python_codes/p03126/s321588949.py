n, m = map(int, input().split())
a = list(map(int, input().split()))
del a[0]
if n != 1:
  for i in range(n-1):
    b = list(map(int, input().split()))
    del b[0]
    a = a+b
    a = [x for x in set(a) if a.count(x) > 1]
print(len(a))