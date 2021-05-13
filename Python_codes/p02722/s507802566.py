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
    n = int(ipt())
    if n == 2:
        print(1)
        exit()

    def al_div(n):
        pn = 1
        div = []
        while pn**2 < n:
            if n%pn == 0:
                div.append(pn)
                div.append(n//pn)
            pn += 1
        if pn**2 == n:
            div.append(pn)
        return div
    ans = 0
    for i in al_div(n-1):
        if i == 1:
            continue
        else:
            if n%i == 1:
                ans += 1
    for i in al_div(n):
        if i == 1:
            continue
        ni = n
        while ni%i == 0:
            ni //= i
        if ni%i == 1:
            ans += 1

    print(ans)

    return

if __name__ == '__main__':
    main()
