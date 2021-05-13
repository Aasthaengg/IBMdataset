a, b = map(int, input().split())
ans = []
def paintW():
  a_count = 1
  for i in range(50, 100):
    if a_count == a:
      return
    for j in range(1, 101):
      if not ans[i+1][j] == '.' and not ans[i-1][j] == '.' and not ans[i][j+1] == '.' and not ans[i][j-1] == '.' and not ans[i-1][j-1] == '.' and not ans[i-1][j+1] == '.' and not ans[i+1][j-1] == '.' and not ans[i+1][j+1] == '.':
        ans[i][j] = '.'
        a_count += 1
      if a_count == a:
        return
def paintB():
  b_count = 1
  if b_count == b:
    return
  for i in range(1, 50):
    for j in range(1, 101):
      if not ans[i+1][j] == '#' and not ans[i-1][j] == '#' and not ans[i][j+1] == '#' and not ans[i][j-1] == '#' and not ans[i-1][j-1] == '#' and not ans[i-1][j+1] == '#' and not ans[i+1][j-1] == '#' and not ans[i+1][j+1] == '#':
        ans[i][j] = '#'
        b_count += 1
      if b_count == b:
        return
ans.append(['*']*102)
for i in range(50):
  ans.append(['*'] + ['.']*100 + ['*'])

for i in range(50):
  ans.append(['*'] + ['#']*100 + ['*'])
ans.append(['*']*102)

paintB()
paintW()

print(100, 100)
for i in range(1, len(ans)-1):
  print(''.join(ans[i][1:101]))