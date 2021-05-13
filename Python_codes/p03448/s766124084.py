a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
for i500 in range(a+1):
  for i100 in range(b+1):
    for i50 in range(c+1):
      total = (i500*500) + (i100*100) + (i50*50)
      if total == x:
        cnt += 1

print(cnt)