import sys
input = sys.stdin.readline
from collections import Counter
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

N,K,L = map(int,input().split())

PQ = [[int(x) for x in input().split()] for _ in range(K)]
RS = [[int(x) for x in input().split()] for _ in range(L)]

P,Q = zip(*PQ)
R,S = zip(*RS)

g1 = csr_matrix(([1]*K,(P,Q)),(N+1,N+1))
g2 = csr_matrix(([1]*L,(R,S)),(N+1,N+1))

_,comp1 = connected_components(g1,directed = False,return_labels = True)
_,comp2 = connected_components(g2,directed = False,return_labels = True)

comp_pair = comp1.astype('int64') * (N+1) + comp2
c = Counter(comp_pair)

answer = [c[comp_pair[i]] for i in range(1,N+1)]
print(*answer)