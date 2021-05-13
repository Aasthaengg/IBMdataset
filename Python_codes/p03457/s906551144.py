N = int(input())
TXY = [list(map(int, input().split())) for _ in range(N)]
 
pre_t, pre_x, pre_y = 0, 0, 0
for t, x, y in TXY:
  diff_t = t - pre_t
  diff_pos = abs(x-pre_x) + abs(y-pre_y)
  if diff_t < diff_pos or (diff_t-diff_pos) % 2 == 1:
    print('No')
    exit()
  else:
    pre_t, pre_x, pre_y = t, x, y
print('Yes')