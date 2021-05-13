import sys
from collections import defaultdict
import math

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    g = A[0]

    for i in range(1,N):
        g = math.gcd(g,A[i])

    print(g)





if __name__ == "__main__":
    main()
