#import numpy as np
#from numpy import*
#from scipy.sparse.csgraph import shortest_path #shortest_path(csgraph=graph) # dijkstra# floyd_warshall
#from scipy.sparse import csr_matrix
 
from collections import* #defaultdict Counter deque appendleft
from fractions import gcd
from functools import* #reduce
from itertools import* #permutations("AB",repeat=2) combinations("AB",2) product("AB",2) groupby accumulate
from operator import mul,itemgetter
from bisect import* #bisect_left bisect_right
from heapq import* #heapify heappop heappushpop
from math import factorial,pi
from copy import deepcopy
import sys
sys.setrecursionlimit(10**8)
#input=sys.stdin.readline  #危険！基本オフにしろ！
 
def main():
    k=int(input())
    ans=list(range(1,51))
    ans[49-k%50]-=1
    for i in range(50):
        ans[i]+=(k//50)
    
    print(50)
    print(*ans)
if __name__ == '__main__':
    main()