# -*- coding: utf-8 -*-
# 整数の入力
N = int(input())
infos = []
for i in range(N):
  infos.append([int(s) for s in input().split()])

def check():
    c_t = 0
    c_x = 0
    c_y = 0
    for info in infos:
      n_t = info[0]
      n_x = info[1]
      n_y = info[2]

      d_t = n_t - c_t
      d_x = abs(n_x - c_x)
      d_y = abs(n_y - c_y)
      if d_t < (d_x + d_y):
        return "No"

      if (d_t - (d_x+d_y)) % 2 != 0:
        return "No"
      c_t = n_t
      c_x = n_x
      c_y = n_y
    return "Yes"

print(check())
