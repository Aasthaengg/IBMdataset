N = int(input())
s = [(input()) for _ in range(N)]
ans = 0
a_cnt = 0
b_cnt = 0
ab_cnt = 0
for i in range(N):
  if s[i][0] == 'B' and s[i][-1] == 'A':
    ab_cnt += 1
  elif s[i][0] == 'B':
    b_cnt += 1
  elif s[i][-1] == 'A':
    a_cnt += 1
  for j in range(len(s[i])-1):
    if s[i][j] + s[i][j+1] == 'AB':
      ans += 1
if ab_cnt == 0:
  print(ans + min(a_cnt, b_cnt))
else:
  ans += ab_cnt - 1 
  if a_cnt > 0:
    ans += 1
    a_cnt -= 1
  if b_cnt > 0:
    ans += 1
    b_cnt -= 1
  ans += min(a_cnt, b_cnt)
  print(ans)
