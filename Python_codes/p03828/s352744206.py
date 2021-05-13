import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush


n = int(input())
array = [0]*(n+1)

def prime_factor(n):
    for i in range(2, int(n**0.5)+1):
        while n%i == 0:
            array[i] += 1
            n //= i
    if n != 1:
        array[n] += 1

def main():
    for i in range(1, n+1):
        prime_factor(i)
    ans = 1
    for i in range(len(array)):
        ans *= array[i]+1
    print(ans%(10**9+7))


if __name__ == '__main__':
    main()
