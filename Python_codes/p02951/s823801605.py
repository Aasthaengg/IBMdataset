import sys
import math
import bisect

def main():
    a, b, c = map(int, input().split())
    if a - b <= c:
        c -= a - b
        b = a
    else:
        b += c
        c = 0
    print(c)
    
if __name__ == "__main__":
    main()
