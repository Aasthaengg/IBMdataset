# -*- coding: utf-8 -*-
S = input()

max_raindays_in_row = 0
raindays_in_row = 0

for s in S:
    if s == 'R':
        raindays_in_row += 1
    else:
        if max_raindays_in_row < raindays_in_row:
            max_raindays_in_row = raindays_in_row
        raindays_in_row = 0
else:
    if max_raindays_in_row < raindays_in_row:
        max_raindays_in_row = raindays_in_row

print(max_raindays_in_row)