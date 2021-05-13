# -*- coding: utf-8 -*-

sx, sy, tx, ty = map(int, input().split())

# s to t 1回目
route_x = tx - sx
route_y = ty - sy
print('U' * route_y, end='') # ↑
print('R' * route_x, end='') # →

# t to s 1回目
print('D' * route_y, end='') # ↓
print('L' * route_x, end='') # ←

# s to t 2回目
print('L', end='') # ←
print('U' * (route_y + 1), end='') # ↑
print('R' * (route_x + 1), end='') # →
print('D', end='') # ↓

# t to s 2回目
print('R', end='') # →
print('D' * (route_y + 1), end='') # ↓
print('L' * (route_x + 1), end='') # ←
print('U', end='')