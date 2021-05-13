n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cost0 = 0
costN = 0
for a_i in a:
  if a_i < x:
    cost0 += 1
  elif a_i > x:
    costN += 1
print(min(cost0, costN))