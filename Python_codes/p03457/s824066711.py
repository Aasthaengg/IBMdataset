n = int(input())
curt, curx, cury = 0, 0, 0
ans = 'Yes'
for _ in range(n):
   t, x, y = map(int, input().split())
   d = abs(x - curx) + abs(y - cury)
   if d > (t - curt) or (t - curt) % 2 != d % 2:
      ans = 'No'
      break
   curt, curx, cury = t, x, y

print(ans)
