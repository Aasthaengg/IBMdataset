import sys
import math
import bisect

def main():
    ans = 0
    for a in list(map(int, input().split())):
        ans ^= a
    print(ans)
    
if __name__ == "__main__":
    main()
