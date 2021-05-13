a, b, c = input().split()
k = int(input())

for _ in range(k):
  if int(a) >= int(b):
    b = int(b) * 2
  else:
    c = int(c) * 2
    
if int(a) < int(b) and int(b) < int(c):
  print("Yes")
else:
  print("No")