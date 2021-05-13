K, T = map(int, input().split())
a = list(map(int, input().split()))

x = max(a)
a.pop(a.index(max(a)))
y = sum(a)

if x > y:
  print(x-y-1)
else:
  print(0)