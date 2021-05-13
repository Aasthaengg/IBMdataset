import sys
import math
from collections import defaultdict,deque

input = sys.stdin.readline
def inar():
    return [int(el) for el in input().split()]
def main():
    n=list(input().strip())
    if "7" in n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()



