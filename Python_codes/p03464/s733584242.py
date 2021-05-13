from math import floor, ceil
k = int(input())
a = [int(i) for i in input().split()]
l,r = 2,2
for ai in a[::-1]:
    xi = ceil(l/ai)
    yi = floor(r/ai)
    if xi > yi:
        print(-1)
        exit()
    l = xi * ai
    r = yi * ai + ai - 1
print(l, r)