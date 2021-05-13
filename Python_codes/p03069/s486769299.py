n = int(input())
s = input()
b_total = 0
w_total = 0
ans = 0
for i in range(n):
  if s[i] == '#':
    b_total += 1
  if s[i] == '.':
    w_total += 1
if b_total == n:
  print(0)
else:
  b_cnt = 0
  w_cnt = 0
  ans = b_cnt + (w_total - w_cnt)
  for i in range(n):
    if s[i] == '#':
      b_cnt += 1
    if s[i] == '.':
      w_cnt += 1
    cnt = b_cnt + (w_total - w_cnt)
    ans = min(ans, cnt)
  print(ans)
