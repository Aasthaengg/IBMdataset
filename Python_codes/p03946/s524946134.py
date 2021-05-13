# import numpy as np
# import math
import sys
input = sys.stdin.readline

def main():
    N,T = map(int,input().split())
    A = list(map(int,input().split()))

    maxgain = 0
    time = 0
    maxcost = A[0]
    mincost = A[0]

    for now in A:
        # print(now)
        maxcost = max(maxcost,now)
        mincost = min(mincost,now)
        temp = now - mincost
        # print(temp)
        if maxgain == temp:
            time += 1
        elif maxgain < temp:
            maxgain = temp
            time = 1
        # print(maxgain)
        # print(time)

    print(time)



main()
