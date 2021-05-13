import sys
import math
import bisect

def main():
    A = input().split()
    B = []
    for a in A:
        B.append(a[0].upper())
    print(''.join(B))
 
if __name__ == "__main__":
    main()
