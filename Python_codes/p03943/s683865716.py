import sys
import math
import bisect

def solve(A):
    for a in A:
        if a * 2 == sum(A):
            return True
    return False
 
def main():
    A = list(map(int, input().split()))
    if solve(A):
        print('Yes')
    else:
        print('No')
 
if __name__ == "__main__":
    main()
