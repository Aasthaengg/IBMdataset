n, m = map(int, input().split())
a = list(map(int, input().split()))

a_sum = sum(a)
asobi = n - a_sum

if asobi >= 0:
  print(asobi)
else:
  print(-1)