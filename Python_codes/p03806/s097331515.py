# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n,A,B = [int(i) for i in readline().split()]
abc = [[int(i) for i in readline().split()] for j in range(n)]

ans = 10**9

d = {0:0}
for i in range(n):
    nd = {}
    a,b,c = abc[i]
    for amari,yen in d.items():
        if amari in nd:
            nd[amari] = min(nd[amari],yen)
        else:
            nd[amari] = yen

        yen += c
        amari += a*B-b*A
        if amari == 0 and yen != 0:
            ans = min(ans,yen)
        elif amari in nd:
            nd[amari] = min(nd[amari],yen)
        else:
            nd[amari] = yen
    d = nd
#    print(d,nd)

if ans == 10**9:
    print(-1)
else:
    print(ans)



