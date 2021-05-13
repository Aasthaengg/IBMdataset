import sys
n = int(input())
a,b,c = sys.stdin
count = 0
for i in range(n):
  if a[i] == b[i] == c[i]:
    continue
  elif a[i] == b[i] or a[i] == c[i] or b[i] == c[i]:
    count += 1
  else:
    count += 2
print(count)