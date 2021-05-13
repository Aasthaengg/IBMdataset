n = int(input())
h = list(map(int, input().split()))

move = [0]
cnt = 0

for i in range(n-1):
  if h[i] >= h[i+1]:
    cnt += 1
    if i == n-2:
      move.append(cnt)
  else:
    move.append(cnt)
    cnt = 0


print(max(move))