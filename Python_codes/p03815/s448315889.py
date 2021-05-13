x = int(input())
cnt = (x-1) // 11
mod = (x-1) % 11

if mod <= 5:
  ans = 2 * cnt + 1
else:
  ans = 2 * cnt + 2
print(ans)