# -*- coding: <encoding name> -*-

line_1 = input()
line_2 = input()
line = line_1 + line_2
print('YES' if line == line[::-1] else 'NO')