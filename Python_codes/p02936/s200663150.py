import numpy as np
import sys
i4 = np.int32

if sys.argv[-1] == 'ONLINE_JUDGE':
    adjacency_list = '''
import numpy as np
from numba import njit
from collections import namedtuple

AdjacencyList = namedtuple('AdjacencyList', ['v', 'adj'])

@njit
def adjacency_list(n, a):
    """
    隣接リストの作成
    :param n: vertex の数
    :param a: 2d の ndarray, 各行は、[u, v] u: Edge の始点、v: Edge の終点
    :return: AdjacencyList
    """
    v = np.zeros(n + 1, np.int32)
    for i in range(a.shape[0]):
        v[a[i, 0] + 1] += 1
    for i in range(1, v.shape[0]):
        v[i] += v[i - 1]
    adj = np.empty(a.shape[0], np.int32)
    temp = np.zeros(n, np.int32)
    for i in range(a.shape[0]):
        from_ = a[i, 0]
        adj[v[from_] + temp[from_]] = a[i, 1]
        temp[from_] += 1
    return AdjacencyList(v, adj)


@njit
def at(gc, n):
    return gc.adj[gc.v[n]:gc.v[n + 1]]


@njit
def iter(gc, n):
    for i in range(gc.v[n], gc.v[n + 1]):
        yield gc.adj[i]        
    '''
    import os
    os.makedirs('nbacl/graphs', exist_ok=True)
    with open('nbacl/graphs/adjacency_list.py', 'w') as f:
        f.write(adjacency_list)

    abc138_d_numba = '''
import numpy as np
import nbacl.graphs.adjacency_list as tree
from numba import njit
from numba.types import Array, int32
from numba.pycc import CC
i4 = np.int32
cc = CC('abc138_d_numba')


@njit
def dfs(d, prev, v, adj, u, val):
    y = val[d]
    for i in range(v[d], v[d + 1]):
        x = adj[i]
        if x == prev:
            continue
        val[x] = y + u[x]
        dfs(x, d, v, adj, u, val)


@cc.export('solve', (Array(int32, 2, 'C'), Array(int32, 2, 'C'), int32))
def solve(a, p, N):
    tr = tree.adjacency_list(N, a)
    u = np.zeros(N, i4)
    val = np.zeros(N, i4)
    for i in range(p.shape[0]):
        u[p[i, 0] - 1] += p[i, 1]
    val[0] = u[0]
    dfs(int32(0), int32(-1), tr.v, tr.adj, u, val)
    return val


if __name__ == '__main__':
    cc.compile()
    '''
    with open('abc138_d_numba.py', 'w') as f:
        f.write(abc138_d_numba)
    import subprocess
    cmd = "python3.8 abc138_d_numba.py"
    subprocess.run(cmd.split())
    exit(0)


from abc138_d_numba import solve

def main():
    f = open(0)
    N, Q = [int(x) for x in f.readline().split()]
    ap = np.fromstring(f.read(), i4, sep=' ').reshape((-1, 2))
    a = ap[:N - 1] - 1
    a = np.concatenate((a, a[:, ::-1]))
    p = ap[N - 1:]
    val = solve(a, p, N)
    print(*val.tolist())


if __name__ == '__main__':
    main()
