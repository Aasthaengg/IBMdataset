n = int(input())
key = [0]*n
flag = True
ans = 0
for i in range(n):
  a = int(input())
  if i == 0:
    if a != 0:
      flag = False
      break
    continue
  if a > key[i-1]+1:
    flag = False
    break
  key[i] = a
  if a == 1:
    ans += 1
  elif a == key[i-1]+1:
    ans += 1
  else:
    ans += a
if flag:
  print(ans)
else:
  print(-1)