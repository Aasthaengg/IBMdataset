#!/usr/bin/env python3
s = int(input())
if s <= 10**9:
    print(s, 0, 0, 0, 0, 1)
else:
    print(10**9, 1*(s<10**18), 10**9 - int(str(s)[-9:]), s // 10**9 + 1*(s<10**18),0,0)
