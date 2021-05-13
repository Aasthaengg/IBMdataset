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
    s = input()
    l = 0
    r = len(s)-1
    ans = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == "x":
            l += 1
            ans += 1
        elif s[r] == "x":
            r -= 1
            ans += 1
        else:
            print(-1)
            exit()
    print(ans)
    return

if __name__ == '__main__':
    main()
