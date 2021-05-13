# -*- coding: utf-8 -*-

N = int(input())
c = input()

r_total = 0
w_total = 0
for i in c:
  if i == 'R':
    r_total += 1
  elif i == 'W':
    w_total += 1

w_left = 0
r_left = 0

ans = r_total # 仕切りが左端の場合

# iが仕切りの位置
for i in range(N):
  cnt = 0
  if c[i] == 'R':
    r_left += 1
    
  elif c[i] == 'W':
    w_left += 1
    
  if w_left <= r_total - r_left:
    cnt += w_left # 仕切りより左の白と右の赤を入れ替え
    cnt += (r_total - r_left) - w_left # 仕切りより右の赤を白に変更
  else:
    cnt += r_total - r_left  # 仕切りより左の白と右の赤を入れ替え
    cnt += w_left - (r_total - r_left) # 仕切りより左の白を赤に変更
  ans = min(ans, cnt)
print(ans)