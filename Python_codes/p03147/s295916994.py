#!/usr/bin/env python3

n = int(input())
h = list(map(int, input().split()))

def isallzero(h):
    ans = True
    for i in h:
        if i != 0:
            ans = False
            break
    return ans 

def func(h):
    if isallzero(h):
        return -1
    for i in range(len(h)):
        if h[i] != 0:
            return i

ans = -1
while True:
    ans += 1
#    print('h =', h)
#    print('isallzero() =', isallzero(h))
    if isallzero(h):
        break

    m = func(h)
    for i in range(m, n): 
        if h[i] != 0:
            h[i] -= 1
        else:
            break

print(ans)