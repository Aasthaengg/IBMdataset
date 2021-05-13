from math import sqrt, floor, ceil
n = int(input())
cnt = 0
div = 1
while div < (n - div) // div:
    if (n - div) % div == 0:
        cnt += (n - div) // div
    div += 1
print(cnt)