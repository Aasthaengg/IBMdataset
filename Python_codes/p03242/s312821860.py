def replace1and9(x):
  if x == '9':
    return '1'
  if x == '1':
    return '9'

n = input()
ans = ""
for i in n:
  ans += replace1and9(i)
print(ans)