n = int(input())
a = [int(x) for x in input().split()]

num = {}
for v in a:
  if v in num:
    num[v] = num[v] + 1
  else:
    num[v] = 1
m = int(input())
t = [int(x) for x in input().split()]

ok = True
for v in t:
  if v not in num:
    ok = False
  elif num[v] <= 0:
    ok = False
  else:
    num[v] = num[v] - 1

if ok:
  print("YES")
else:
  print("NO")
