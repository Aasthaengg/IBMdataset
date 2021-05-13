n = int(input())
a = list(map(int,input().split()))
x = list(set(a))
x.sort()
if len(x) >= 4:
  print("No")
  exit()
if len(x) == 3:
  if x[0]^x[1] == x[2] and 3*a.count(x[0]) == 3*a.count(x[1]) == 3*a.count(x[2]) == n:
    print("Yes")
  else:
    print("No")
  exit()
if len(x) == 2:
  if x[0] == 0 and (2*a.count(x[0]) == 2*a.count(x[1]) == n or 6*a.count(x[0]) == 3*a.count(x[1]) == 2*n):
    print("Yes")
  else:
    print("No")
  exit()
if len(x) == 1:
  if x[0] == 0:
    print("Yes")
  else:
    print("No")