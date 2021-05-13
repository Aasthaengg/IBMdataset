n = int(input())
a = list(input())
cnt_r = n-1
cnt_l = 0
cnt = 0
while True:
  if cnt_r == cnt_l:
    print(cnt)
    exit()
  if a[cnt_r] == 'W':
    cnt_r -= 1
    continue
  if a[cnt_l] == 'R':
    cnt_l += 1
    continue
  a[cnt_r], a[cnt_l] = a[cnt_l], a[cnt_r]
  cnt += 1