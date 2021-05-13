# C - Otoshidama

n,y = map(int,input().split())

import sys

tmp = y - 1000*n

a = y // 10000

for i in reversed(range(a+1)):
    for j in range((y - 10000*i) // 5000 + 1):
        if 9000*i + 4000*j == tmp:
            print(i,j,n-i-j)
            sys.exit()
print(-1,-1,-1)
