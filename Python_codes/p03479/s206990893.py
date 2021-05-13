import math
x,y=map(int,input().split())
for p in range(61):
    if 2**p>y//x:
        print(p)
        exit(0)