h, w = map(int, input().split())
s = []
for i in range(h):
  l = input()
  s.append(list(l))
ans = ''
for i in range(h):
  if ans == '':
    for j in range(w):
      if ans == '' and s[i][j] == '#':
        f = 0
        if i - 1 >= 0 and s[i - 1][j] == '#':
          f += 1
        if j - 1 >= 0 and s[i][j - 1] == '#':
          f += 1
        if j + 1 <= w - 1 and s[i][j + 1] == '#':
          f += 1
        if i + 1 <= h - 1 and s[i + 1][j] == '#':
          f += 1
        if f == 0:
          ans = 'No'
        else:
          next
      elif ans == '' and s[i][j] == '.':
        next
if ans == '':
  ans = 'Yes'
print(ans)