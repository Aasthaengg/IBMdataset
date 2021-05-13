import math

size = {}
size['H'] = int(input())
size['W'] = int(input())
N = int(input())
if size['H'] > size['W']:
    bigsize = 'H'
else:
    bigsize = 'W'
lines_num = math.ceil(N/size[bigsize])

print(lines_num)
