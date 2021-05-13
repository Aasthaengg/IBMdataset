import sys
from collections import defaultdict
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

N, K, L = map(int, input().split())
pq_and_rs = list(map(int, read().split()))

ps = pq_and_rs[:2*K:2]
qs = pq_and_rs[1:2*K:2]
rs = pq_and_rs[2*K::2]
ss = pq_and_rs[2*K+1::2]

pq_adj = csr_matrix(([1] * (2 * K), (ps + qs, qs + ps)), shape=(N+1, N+1))
rs_adj = csr_matrix(([1] * (2 * L), (rs + ss, ss + rs)), shape=(N+1, N+1))

group = ((connected_components(pq_adj)[1].astype(np.int64) << 32) + connected_components(rs_adj)[1]).tolist()
group_to_elements = defaultdict(list)
for v, g in enumerate(group):
    group_to_elements[g].append(v)

for v in range(1, N+1):
    print(len(group_to_elements[group[v]]))