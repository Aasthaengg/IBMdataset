n = int(input())
a = list(map(int, input().split()))
ans = 1
if n == 1 or n == 2:
  ans = 1
else:
  b = [a[0], a[1]]
  if a[1] - a[0] > 0:
    f = '+'
  elif a[1] - a[0] < 0:
    f = '-'
  elif a[1] - a[0] == 0:
    f = ''
  for i in range(2, n):
    if f == '+' and a[i] - b[-1] >= 0:
      b.append(a[i])
      f = '+'
    elif f == '+' and a[i] - b[-1] < 0:
      b = [a[i]]
      f = ''
      ans += 1
    elif f == '-' and a[i] - b[-1] <= 0:
      b.append(a[i])
      f = '-'
    elif f == '-' and a[i] - b[-1] > 0:
      b = [a[i]]
      f = ''
      ans += 1
    elif f == '' and a[i] - b[-1] > 0:
      b.append(a[i])
      f = '+'
    elif f == '' and a[i] - b[-1] < 0:
      b.append(a[i])
      f = '-'
    elif f == '' and a[i] - b[-1] == 0:
      b.append(a[i])
      f = ''
print(ans)