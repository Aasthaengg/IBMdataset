# D - FT Robot

import copy

s = input()
x, y = map(int, input().split())

f = [len(x) for x in s.split("T")]
x -= f[0]
fx = f[2::2]
fy = f[1::2]

x_possible_set = set([0])
for dx in fx:
    tmp = set()
    for current_x in x_possible_set:
        tmp.add(current_x + dx)
        tmp.add(current_x - dx)
    x_possible_set = tmp.copy()

y_possible_set = set([0])
for dy in fy:
    tmp = set()
    for current_y in y_possible_set:
        tmp.add(current_y + dy)
        tmp.add(current_y - dy)
    y_possible_set = tmp.copy()

print("Yes" if x in x_possible_set and y in y_possible_set else "No")