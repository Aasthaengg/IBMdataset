import math
import collections
import itertools
import heapq

def main():
    N = int(input())
    A = list(map(int, input().split()))

    prod = 1
    for a in A:
        prod *= a
    prod_div_a = [0] * N
    for i in range(N):
        prod_div_a[i] = prod // A[i]
    res = prod / sum(prod_div_a)
    print(res)
    

if __name__ == "__main__":
    main()