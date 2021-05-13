import sys
import math
from collections import defaultdict,deque

input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
def find(a,b,c):
    gc=math.gcd(a,b)
    return math.gcd(gc,c)
def main():
    k=int(input())
    ans=0
    for i in range(1,k+1):
        for j in range(1,k+1):
            for k in range(1,k+1):
                ans+=find(i,j,k)
    print(ans)


if __name__ == '__main__':
    main()



