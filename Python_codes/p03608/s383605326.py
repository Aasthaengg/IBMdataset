n,m,R = map(int,input().split())
r = list(map(int,input().split()))

from itertools import permutations
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
cost = np.ones((n,n))*float('inf')
for i in range(m):
    a,b,c = map(int,input().split())
    cost[a-1][b-1]=cost[b-1][a-1]=c
d = floyd_warshall(cost)
def main():
    m = float('inf')

    for j in permutations(r):
        l = 0
        for i in range(len(j)-1):
            s,t = j[i],j[i+1]
            l += d[s-1][t-1]
        if l<m:
            m = l
    print(int(m))


if __name__ == "__main__":
    main()