import sys
from collections import Counter
import bisect


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())

    W_max =0
    W_min= 10**9+7
    Y_max= -10**9-1
    Y_min=10**9+7

    for i in range(N):
        x,y =map(int,input().split())
        W_max =max(W_max,x+y)
        W_min =min(W_min,x+y)
        Y_max =max(Y_max,x-y)
        Y_min =min(Y_min,x-y)

    print(max(W_max - W_min,Y_max - Y_min))






if __name__ == "__main__":
    main()
