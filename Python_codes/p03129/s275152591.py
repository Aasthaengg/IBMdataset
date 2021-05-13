import sys
import math
import bisect

def main():
    n, m = map(int, input().split())
    if (n + 1) // 2 >= m:
        print('YES')
    else:
        print('NO')
    
if __name__ == "__main__":
    main()
