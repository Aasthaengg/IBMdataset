from math import ceil

S = int(input())
ax, ay = 10 ** 9 , 1
by = ceil(S / 10 ** 9)
bx = 10 ** 9 * by - S
print(0, 0, ax, ay, bx, by)
