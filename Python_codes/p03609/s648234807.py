import sys
import math
import bisect

def main():
    x, t = map(int, input().split())
    print(max(0, x - t))

if __name__ == "__main__":
    main()
