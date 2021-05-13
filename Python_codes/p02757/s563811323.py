#!/usr/bin/python3

(n, p) = map(int, input().split())
s = input()

c = 0
if p == 2 or p == 5:
    for i in range(n - 1, -1, -1):
        if int(s[i]) % p == 0:
            c += i + 1

else:
    mm = {}
    r = 0
    mten = 1
    for i in range(n - 1, -1, -1):
        ch = int(s[i])
        r = (r + ch * mten) % p
        mten = (mten * 10) % p
        if r in mm:
            c += mm[r]
            mm[r] += 1
        else:
            mm[r] = 1

        if r == 0:
            c += 1
        
print(c)
