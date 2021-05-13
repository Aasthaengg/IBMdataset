n = int(input())
a = list(map(int, input().split()))

cnt = 0
if n == 1:
  print (1)
  exit()
c = 0
for i in range(n-1):
  if c == 2 and a[i+1] < a[i]:
    cnt += 1
    c = -1
  elif c == 1 and a[i+1] > a[i]:
    cnt += 1
    c = -1
  else:
    if c < 1:
      if a[i+1] > a[i]:
        c = 2
      elif a[i+1] == a[i]:
        c = 0
      else:
        c = 1
print (cnt+1)