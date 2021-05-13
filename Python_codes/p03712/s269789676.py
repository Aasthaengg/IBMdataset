H, W = map(int, input().split())
data = []
for i in range(H):
  data.append(input().split())
print("#" * (W+2))
for i in range(H):
  print("#", end='')
  for j in data[i]:
    print(j, end='')
  print("#")
print("#" * (W + 2))