import sys
import math
import bisect

def main():
    a, b = map(int, input().split())
    ans = (a + b - 1) // b
    print(ans)

if __name__ == "__main__":
    main()
