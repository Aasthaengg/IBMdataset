import sys
import math
import bisect

def main():
    a, b, c = map(int, input().split())
    ans = 0
    while ans < c and b >= a:
        b -= a
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
