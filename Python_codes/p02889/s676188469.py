import sys
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs= sys.stdin.buffer.readlines
#rstrip().decode('utf-8')

import numpy as np
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
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
#from scipy.sparse.csgraph import csgraph_from_dense
#from scipy.sparse.csgraph import dijkstra
#sys.setrecursionlimit(10**7)

#map(int,input().split())

def main():
    N,M,L=map(int,input().split())
    ABCQST=np.array(read().split(),np.int64)
    ABC=ABCQST[:3*M]
    A=ABC[::3]
    B=ABC[1::3]
    C=ABC[2::3]
    ST=ABCQST[3*M+1:]
    S=ST[::2]
    T=ST[1::2]

    graph1=csr_matrix((C,(A,B)),(N+1,N+1))
    graph1_dist=floyd_warshall(graph1,directed=False)

    graph2=np.full(((N+1),(N+1)),np.inf)
    np.fill_diagonal(graph2,0)
    graph2[graph1_dist<=L+0.5]=1

    graph2_dist=floyd_warshall(graph2,directed=False)
    graph2_dist[graph2_dist==np.inf]=0
    graph2_dist=(graph2_dist+0.5).astype(int)
    ans=graph2_dist[S,T]-1
    print("\n".join(ans.astype(str)))


if __name__ == '__main__':
    main()