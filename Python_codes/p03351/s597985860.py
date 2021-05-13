import sys
a, b, c, d = map(int, input().split())

if a>=c and a-c <= d:
  print("Yes")
  exit()
elif a<c and c-a <= d:
  print("Yes")
  exit()

count = 0
if a>=b and a-b <= d:
  count += 1
elif a<b and b-a <= d:
  count += 1

if b>=c and b-c <= d:
  count += 1
elif b<c and c-b <= d:
  count += 1
  
if count == 2:
  print("Yes")
else:
  print("No")