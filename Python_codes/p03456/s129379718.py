a, b = map(str, input().split())
ab = int(''.join(list(a)+list(b)))

squarelist = []
for i in range(1, 318):
  squarelist.append(i * i)
if ab in squarelist:
  print("Yes")
else:
  print("No")
