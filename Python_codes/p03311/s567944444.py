import sys
input = sys.stdin.readline
from collections import Counter
import math

def main():
    N = int(input())
    A = [int(a) - i for i, a in enumerate(input().split(), 1)]
    A.sort()

    b = A[N//2]
    print(sum(abs(a - b) for a in A))

    
main()