# ABC104D

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))

M = 10**9+7
s = input()
n = len(s)
anum = [None] * n # s[:i+1]のAの数
cnum = [None] * n # s[i+1:]のCの数
hnum1 = [None] * n
hnum2 = [None] * n
acount = 0
ccount = 0
hcount1 = 0
hcount2 = 0
for i,(c,cc) in enumerate(zip(s, s[::-1])):
    if c in "A":
        acount += 1
    if c=="?":
        hcount1 += 1
    anum[i] = acount
    hnum1[i] = hcount1
    if cc in "C":
        ccount += 1
    if cc=="?":
        hcount2 += 1
    cnum[-(i+1)] = ccount
    hnum2[-(i+1)] = hcount2
ans = 0
hn = hnum1[-1]
for i,c in enumerate(s):
    if i in (0, n-1):
        continue
    if c=="B":
        ans += (anum[i-1]*cnum[i+1]*pow(3, hn, M))
        if hn>=1:
            ans += (anum[i-1]*hnum2[i+1]*pow(3, hn-1, M))
            ans += (hnum1[i-1]*cnum[i+1]*pow(3, hn-1, M))
        if hn>=2:
            ans += (hnum1[i-1]*hnum2[i+1]*pow(3, hn-2, M))
    if c=="?":
        ans += (anum[i-1]*cnum[i+1]*pow(3, hn-1, M))
        if hn>=2:
            ans += (anum[i-1]*(hnum2[i+1])*pow(3, hn-2, M))
            ans += (hnum1[i-1]*cnum[i+1]*pow(3, hn-2, M))
        if hn>=3:
            ans += (hnum1[i-1]*hnum2[i+1]*pow(3, hn-3, M))
    ans %= M
#     print(ans)
print(ans)