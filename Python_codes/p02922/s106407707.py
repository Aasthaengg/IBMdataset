a, b = map(int, input().split())

if b == 1:
  cnt = 0
else:
  socket = a
  cnt = 1
  while socket < b:
    socket += (a-1)
    cnt += 1
  
print(cnt)