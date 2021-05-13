import sys
import math
import bisect

def main():
    a = int(input())
    b = int(input())
    if a < b:
        print('LESS')
    elif a > b:
        print('GREATER')
    else:
        print('EQUAL')

if __name__ == "__main__":
    main()
