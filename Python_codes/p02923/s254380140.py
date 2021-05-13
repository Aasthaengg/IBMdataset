N = int(input())
H = list(map(lambda h: int(h), input().split(" ")))
 
lower = [0]
movable = 0
for i in range(len(H) - 1):
  if H[i] >= H[i + 1]:
    movable += 1
  else:
    lower.append(movable)
    movable = 0
else:
  lower.append(movable)

print(max(lower))