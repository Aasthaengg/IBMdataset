arr = list(map(int, input().split()))
flg = 0
for i in range(2):
  a,b = map(int, input().split())
  if arr[0] == a:
    arr.insert(0,b)
  elif arr[0] == b:
    arr.insert(0,a)
  elif arr[-1] == a:
    arr.append(b)
  elif arr[-1] == b:
    arr.append(a)
  elif i == 0:
    flg = 1
if len(arr) == 4 or flg == 1:
  print('YES')
else:
  print('NO')