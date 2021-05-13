import sys
import math
import bisect

def main():
    n, m = map(int, input().split())
    if n % m == 0:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()
