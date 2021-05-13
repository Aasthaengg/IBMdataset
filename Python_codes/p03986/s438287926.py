x = list(input())
cnt = 0
a = 0
for i in x:
  if i == 'S':
    cnt += 1
  elif i == 'T':
    if cnt > 0:
      cnt -= 1
    else:
      a += 1
print(a+cnt)
