import sys

if sys.argv[-1] == 'ONLINE_JUDGE':
    import os
    def write_script(sp):
        if os.path.dirname(sp[1]):
            os.makedirs(os.path.dirname(sp[1]), exist_ok=True)
        with open(sp[1], 'w') as f_write:
            line = f.readline()
            while line:
                if line.startswith("'''"):
                    return
                if line.startswith("###nbacl"):
                    sp = line.split()
                    break
                f_write.write(line)
                line = f.readline()
        write_script(sp)


    with open(__file__) as f:
        line = f.readline()
        while line:
            if line.startswith('###nbacl'):
                sp = line.split()
                write_script(sp)
                break
            line = f.readline()

    import nbmodule
    nbmodule.cc.compile()
    exit(0)


from nbmodule import solve
import numpy as np
i4 = np.int32


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

'''
###nbacl nbacl/graphs/adjacency_list.py
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

###nbacl nbmodule.py
import numpy as np
import nbacl.graphs.adjacency_list as tree
from numba import njit
from numba.types import Array, int32
from numba.pycc import CC
i4 = np.int32
cc = CC('nbmodule')


@njit
def dfs(d, prev, tr, u, val):
    y = val[d]
    for x in tree.iter(tr, d):
        if x == prev:
            continue
        val[x] = y + u[x]
        dfs(x, d, tr, u, val)


@cc.export('solve', (Array(int32, 2, 'C'), Array(int32, 2, 'C'), int32))
def solve(a, p, N):
    tr = tree.adjacency_list(N, a)
    u = np.zeros(N, i4)
    val = np.zeros(N, i4)
    for i in range(p.shape[0]):
        u[p[i, 0] - 1] += p[i, 1]
    val[0] = u[0]
    dfs(int32(0), int32(-1), tr, u, val)
    return val

'''