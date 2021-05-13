import sys
import math
import bisect

def main():
    ans = 0
    for c in input():
        if c == '+':
            ans += 1
        elif c == '-':
            ans -= 1
    print(ans)

if __name__ == "__main__":
    main()
