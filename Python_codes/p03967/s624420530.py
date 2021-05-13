import sys
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs= sys.stdin.buffer.readlines
#rstrip().decode('utf-8')

#import numpy as np
#import operator
#import bisect
#from heapq import heapify,heappop,heappush
#from math import gcd
#from fractions import gcd
#from collections import deque
#from collections import defaultdict
#from collections import Counter
#from itertools import accumulate
#from itertools import groupby
#from itertools import permutations
#from itertools import combinations
#scipy.sparse import csr_matrix
#scipy.sparse.csgraph import floyd_warshall
#from scipy.sparse.csgraph import csgraph_from_dense
#from scipy.sparse.csgraph import dijkstra
#sys.setrecursionlimit(10**7)

#map(int,input().split())

def main():
    s=input().rstrip().decode('utf-8')
    s0=s[::2]
    s1=s[1::2]
    print(s1.count("g")-s0.count("p"))



if __name__ == '__main__':
    main()