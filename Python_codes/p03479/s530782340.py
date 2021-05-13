import math
x, y = map(int, input().split())
tmp = x
cnt = 0
while y>=tmp:
    tmp = tmp * 2
    cnt += 1
print(cnt)