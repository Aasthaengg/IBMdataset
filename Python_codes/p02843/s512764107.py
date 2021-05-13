X = int(input())
C = 1000000

output = []
for c in range(C):
    if (c*100) <= X <= (c*105):
        output.append(1)
    else:
        output.append(0)
if max(output):
  print("1")
else:
  print("0")