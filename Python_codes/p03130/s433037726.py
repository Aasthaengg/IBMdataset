box = [0] * 5
for i in range(3):
  a, b = map(int, input().split())
  box[a] += 1
  box[b] += 1
if max(box) > 2:
  print("NO")
else:
  print("YES")