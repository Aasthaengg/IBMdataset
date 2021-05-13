n = int(input())
arr = list(map(int, input().split()))
r = 0
cols = [0] * 8
for i in arr:
  color = i // 400
  if color <= 7:
    cols[color] = 1
  else:
    r += 1
c = sum(cols)
print(max(1, c), r+c)