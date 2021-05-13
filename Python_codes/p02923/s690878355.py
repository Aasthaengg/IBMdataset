import sys

# import bisect
# import numpy as np
from collections import deque
# map(int, sys.stdin.read().split())



def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())
    H = list(map(int,input().split()))

    con = 0
    ans =0
    for i in range(N-1):
        if H[i] >=H[i+1]:
            con +=1
            ans =max(ans,con)
        else:
            con =0

    print(ans)



if __name__ == "__main__":
    main()
