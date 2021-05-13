import sys
from collections import Counter
import bisect


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N=int(input())
    D,X=map(int,input().split())
    ans =0
    for i in range(N):
        a =int(input())
        ans+=1 + (D-1)//a


    print(ans+X)




if __name__ == "__main__":
    main()
