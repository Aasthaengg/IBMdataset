import sys
import numpy as np
# from decimal import Decimal
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
# ----------------------------------------
n = int(readline())
#s = readline()
# print(s)
s = input()

ans = 0
x = 0
for i in range(n):
    tar = s[i]
    if (tar == 'I'):
        x += 1
    else:
        x -= 1

    ans = max(x, ans)
    # print(ans)


print(ans)
