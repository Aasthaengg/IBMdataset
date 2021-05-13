n = int(input())
a = list(map(int,input().split()))
state = 100
count = 1
tmp = a[0]
for i in a:
  if i == tmp:
    pass
  elif i > tmp:
    if state == 1:
      pass
    elif state == 0:
      count += 1
      state = 100
    else:
      state = 1
  else:
    if state == 0:
      pass
    elif state == 1:
      count += 1
      state = 100
    else:
      state = 0
  tmp = i
print(count)