n = int(input())
a = [int(input()) for _ in range(n)]

ans = -1
visited = set()
count = 0
btn = 0
for i in range(n):
  if btn in visited:
    break
  visited.add(btn)
  btn = a[btn]-1
  count += 1
  if btn == 1:
    ans = count
    break

print(ans)
