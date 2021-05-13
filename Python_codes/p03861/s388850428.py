#!/usr/bin/env python

a, b, x = map(int, input().split())

if a == b:
    if a%x == 0:
        print(1)
    else:
        print(0)
    exit()
if a%x == 0 and b%x == 0:
    ans = b//x - a//x + 1 
    print(ans)
    exit()
if a%x != 0 and b%x != 0:
    ans = b//x - a//x
    print(ans)
    exit()
if a%x == 0 and b%x != 0:
    ans = b//x - a//x + 1 
    print(ans)
    exit()
ans = b//x - a//x 
print(ans)
