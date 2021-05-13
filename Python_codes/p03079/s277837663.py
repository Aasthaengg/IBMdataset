a = list(map(int,input().split()))

tri = 0

if a[0] == a[1]:
  if a[1] == a[2]:
    tri += 1
    
if tri == 0:
  print("No")
else:
  print("Yes")    