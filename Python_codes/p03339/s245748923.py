n = int(input())
s = list(input())
a = [0]*n
for i in range(n):
  if s[i] == 'E':
    a[i] = a[i-1]+1
  else:
    a[i] = a[i-1]
b = [0]*n
for i in range(n):
  if i == 0:
    b[i] = a[n-1] - a[i]
  elif i == n-1:
    b[i] = i - a[i-1]
  else:
    b[i] = i - a[i-1] + a[n-1] - a[i]
print(min(b))