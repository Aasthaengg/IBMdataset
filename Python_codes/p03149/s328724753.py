import sys
import math
import bisect

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A == sorted([1, 9, 7, 4]):
        print('YES')
    else:
        print('NO')
    
if __name__ == "__main__":
    main()
