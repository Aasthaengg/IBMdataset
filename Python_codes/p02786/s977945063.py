from collections import deque
h=int(input())
d=dict()
def solve(h):
    if h==1:
        return 1
    else:
        l=h//2
        if l not in d.keys():
            d[l]=solve(l)
        return d[l]*2+1

print(solve(h))