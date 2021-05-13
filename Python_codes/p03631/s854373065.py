import sys
import math
import bisect

def main():
    s = input()
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
