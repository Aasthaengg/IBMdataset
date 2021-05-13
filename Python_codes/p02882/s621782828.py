# https://atcoder.jp/contests/abc144/tasks/abc144_d

import sys
from math import atan,pi
input=sys.stdin.readline

def main():
    a,b,x=map(int,input().split())
    if 2*x>=b*a**2:
        print(atan((2*(a**2*b-x))/a**3)*180/pi)
    else:
        print(atan(b**2*a/(2*x))*180/pi)
    
    
    
if __name__=="__main__":
    main()
