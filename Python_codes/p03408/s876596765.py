N = int(input())
blue = []
for i in range(N):
  blue.append(input())
M = int(input())
red = []
for i in range(M):
  red.append(input())
ans = 0
for i in range(N):
  count = 0
  for j in range(N):
    if blue[j] == blue[i]:
      count += 1
  for j in range(M):
    if red[j] == blue[i]:
      count -= 1
  if count > ans:
    ans = count
print(ans)