import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    q = int(ipt())

    #√nまでの素数の配列を返す関数
    def primes(n):
        if n < 4:
            return []
        else:
            pri = [2]
            k = 3
            while k*k <= n:
                for i in pri:
                    if k%i == 0:
                        break
                    elif i == pri[-1]:
                        pri.append(k)
                k += 2
            return pri

    p = primes(10**10)
    sm = [0]*100001
    for pi in p[1::]:
        if (pi+1)//2 in p:
            sm[pi] += 1

    for i in range(100000):
        sm[i+1] += sm[i]

    for _ in [0]*q:
        l,r = map(int,ipt().split())
        print(sm[r]-sm[l-1])

    return


if __name__ == '__main__':
    main()
