import sys
import math
import bisect

def main():
    s = ''.join(sorted(list(input())))
    if s == 'abc':
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
