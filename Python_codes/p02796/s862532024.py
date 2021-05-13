n = int(input())
arms = []
for _ in range(n):
  x, l = map(int, input().split())
  arms.append((x-l, x+l))
arms.sort(key=lambda x:x[1])

tmpx = arms[0][1]
ans = 1
for i in range(1, len(arms)):
  if tmpx <= arms[i][0]:
    ans += 1
    tmpx = arms[i][1]

print(ans)


