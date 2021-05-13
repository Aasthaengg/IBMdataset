import sys
#import copy
#import numpy as np
#import itertools
#import collections
#from collections import deque
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
import functools

sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
#read = sys.stdin.buffer.read

mod = 1000000007

def gcd(nums):
    return functools.reduce(euclid, nums)

def euclid(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def main():
    # input
    N, K = map(int, readline().split())

    ans = 0
    count = [0] * K
    for X in range(K,0,-1):
        #tmp = ((K // X) ** N) % mod
        tmp = pow(K//X, N, mod)
        diff = count[X-1::X][1:]
        if len(diff) != 0:
            tmp = (tmp - sum(diff)) % mod
        count[X-1] = tmp

    ans = sum([((x+1)*count[x])%mod for x in range(K)])%mod
    #for X in range(K):
    #    ans = (ans + (X+1) * count[X]) % mod

    #print("end")
    print(ans)


if __name__ == "__main__":
    main()
