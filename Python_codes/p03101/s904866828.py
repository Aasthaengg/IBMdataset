import sys
import math
import bisect

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    ans = H * W - H * w - h * W + h * w
    print(ans)
    
if __name__ == "__main__":
    main()
