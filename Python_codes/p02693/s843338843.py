import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    k = int(input())
    a,b = map(int, input().split())
    for i in range(a,b+1):
        if i%k==0:
            print("OK")
            exit()
    print("NG")






if __name__=="__main__":
    main()
