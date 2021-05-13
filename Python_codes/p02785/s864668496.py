n,k = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
a.reverse()


if n <= k:
  print(0)
else:
  del a[0:k]
  print(sum(a))