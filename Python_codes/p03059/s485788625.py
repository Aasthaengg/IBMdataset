import sys
import math
import bisect

def main():
    a, b, t = map(int, input().split())
    ans = t // a * b
    print(ans)
    
if __name__ == "__main__":
    main()
