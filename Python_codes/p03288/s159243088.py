import sys
import math
import bisect

def main():
    n = int(input())
    if n < 1200:
        print('ABC')
    elif n < 2800:
        print('ARC')
    else:
        print('AGC')

if __name__ == "__main__":
    main()
