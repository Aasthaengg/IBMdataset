n = int(input())
a = list(map(int, input().split()))

flag = [0]*9
t = 0
x = 0
y = 400
while y <= 3200:
  for i in a:
    if x <= i < y: flag[t] = 1
  t += 1
  x += 400
  y += 400
else:
  for i in a:
    if 3200 <= i: flag[8] += 1

if sum(flag[:8]) == 0:
  print(1,flag[8])
  exit()
      
total = sum(flag)
print(total - flag[8], total)