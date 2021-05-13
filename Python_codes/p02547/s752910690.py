n = int(input())
count = 0
t = 1
for _ in range(n):
  a, b = map(int,input().split())
  if a==b:
    count += 1
  if a!=b:
    count = 0
  if count == 3:
    t = 0
if t:
  print("No")
else:
  print("Yes")