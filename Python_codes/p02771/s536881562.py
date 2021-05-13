#import sys
#import numpy as np
#from collections import defaultdict
#import math
#from collections import deque

#input = sys.stdin.readline
#import decimal

def main():
    a,b,c = map(int,input().split())

    if a ==b:
        if a!=c:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    if a ==c:
        if a!=b:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    if b ==c:
        if a!=c:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

    print("No")
if __name__ == "__main__":
    main()