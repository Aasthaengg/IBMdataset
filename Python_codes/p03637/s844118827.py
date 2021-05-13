N = int(input())
a = list(map(int,input().split()))
a4 = a2 = a0 = 0
for i in a:
  if i % 4 == 0:
    a4 += 1
  elif i % 2 == 0:
    a2 += 1
  else:
    a0 += 1
if a2 == 0:
    if a0 <= a4 + 1:
        print("Yes")
    else:
        print("No")
else:
    if a0 <= a4:
        print("Yes")
    else:
        print("No")