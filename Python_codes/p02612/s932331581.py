import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from math import ceil
#import numpy as np
def main():
    n = int(input())
    r = ceil(n / 1000) * 1000 - n
    print(r)

if __name__ == '__main__':
    main()
