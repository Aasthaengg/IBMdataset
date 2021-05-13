import numpy as np
import math

a, b = map(int, input().split())

h = 100
w = 100

char_white = '.'
char_black = '#'

fields_w = [[char_white for _ in range(int(w/2))] for _ in range(h)]
fields_b = [[char_black for _ in range(int(w/2))] for _ in range(h)]

spaces_per_row = math.ceil((int(w/2) - 2) / 2.0)

for i in range(a - 1):
    col = i % spaces_per_row
    row = i // spaces_per_row
    fields_b[row * 2 + 1][col * 2 + 1] = char_white

for i in range(b - 1):
    col = i % spaces_per_row
    row = i // spaces_per_row
    fields_w[row * 2 + 1][col * 2 + 1] = char_black

res = np.concatenate((fields_w, fields_b), 1)

print(str(h) + ' ' + str(w))
for row in res:
    print(''.join(row))
