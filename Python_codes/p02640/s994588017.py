import sys
x,y = map(int,input().split())
flg = 0

for i in range(x+1):
    for j in range(x+1):
        if x == (i+j) and y == (2*i + 4*j):
            print('Yes')
            flg = 0
            sys.exit()
        else:
            flg = 1
if flg:
    print('No')
