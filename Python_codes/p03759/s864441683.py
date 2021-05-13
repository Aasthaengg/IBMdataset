import sys
import math
import bisect

def main():
    a, b, c = map(int, input().split())
    if a + c == b * 2:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
