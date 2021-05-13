import sys
import math
import bisect

def main():
    a, b = map(int, input().split())
    ans = 0
    if a >= b:
        ans += a
        a -= 1
    else:
        ans += b
        b -= 1
    if a >= b:
        ans += a
        a -= 1
    else:
        ans += b
        b -= 1
    print(ans)
    
if __name__ == "__main__":
    main()
