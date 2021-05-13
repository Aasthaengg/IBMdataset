l,r = map(int,input().split())
import sys

if r-l>=2019:
    print(0)
    sys.exit()
else:
    amari = 2018
    for i in range(l,r):
        for j in range(i+1,r+1):
            amari = min(amari,(i*j)%2019)
    print(amari)