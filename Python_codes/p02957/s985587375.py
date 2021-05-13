import sys
import math
import bisect

def main():
    a, b = map(int, input().split())
    if abs(a - b) % 2 == 0:
        k = (a + b) // 2
        print(k)
    else:
        print('IMPOSSIBLE')
    
if __name__ == "__main__":
    main()
