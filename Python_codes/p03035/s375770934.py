import sys
import math
import bisect

def main():
    a, b = map(int, input().split())
    if a <= 5:
        ans = 0
    elif a <= 12:
        ans = b // 2
    else:
        ans = b
    print(ans)
    
if __name__ == "__main__":
    main()
