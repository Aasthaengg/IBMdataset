n, k, c = map(int, input().split())
s = input()
lst = [True] * n
l = []
for i in range(n):
  if s[i] == 'o' and lst[i]:
    l.append(i)
    if len(l) >= k:
      break
    for j in range(c):
      if i + 1 + j < n:
        lst[i+1+j] = False
if len(l) == k:
  lst = [True] * n
  r = []
  for i in range(n - 1, -1, -1):
    if s[i] == 'o' and lst[i]:
      r.append(i)
      if len(r) >= k:
        break
      for j in range(c):
        if i - 1 - j >= 0:
          lst[i-1-j] = False
  if len(r) == k:
    for i in range(k):
      if l[i] == r[k-i-1]:
        print(l[i] + 1)