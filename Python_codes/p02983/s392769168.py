#/usr/bin/env python

L, R = map(int, input().split())
MOD = 2019

if R-L >= MOD:
    print(0)
    exit()

ans = MOD 
tmp = 0 
for i in range(L, R+1):
    for j in range(i+1, R+1):
        tmp = ((i%MOD)*(j%MOD))%MOD
        if tmp <= ans:
            ans = tmp 
print(ans)
