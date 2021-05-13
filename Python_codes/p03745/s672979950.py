n = int(input())
a = list(map(int,input().split()))
c = 1
d = 0
for i in range(n-1):
  if a[i] == a[i+1]:
    pass
  elif a[i] < a[i+1]:
    if d < 0:
      d = 0
      c += 1
    else:
      d += 1
  else:
    if d > 0:
      d = 0
      c += 1
    else:
      d -= 1
print(c)