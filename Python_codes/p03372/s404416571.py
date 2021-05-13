import numpy as np

N,C = list(map(int, input().split()))
XV = [list(map(int, input().split())) for _ in range(N)]
X = np.array([0] + [x for x,v in XV])
V = np.array([0] + [v for x,v in XV])

V_cw_cumsum = V.cumsum()

right_one_ways = V_cw_cumsum - X

V_ccw_cumsum = V[::-1].cumsum()[::-1]

left_one_ways = V_ccw_cumsum - (C-X)

def reduce_each(func, l):
  temp = l.copy()
  for i in range(1,len(l)):
    temp[i] = func(temp[i-1], temp[i])
  return temp


additional_left = np.roll(reduce_each(max, left_one_ways[::-1])[::-1], -1)
additional_left[-1] = 0
right_to_left = V_cw_cumsum - 2*X + additional_left

additional_right = np.roll(reduce_each(max, right_one_ways), 1)
additional_right[0] = 0
left_to_right = V_ccw_cumsum - 2*(C-X) + additional_right

print(max(max(right_one_ways),
          max(left_one_ways),
          max(right_to_left),
          max(left_to_right)))