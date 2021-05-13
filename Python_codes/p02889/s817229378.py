import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
i8 = np.int64
i4 = np.int32


def main():
    stdin = open('/dev/stdin')
    pin = np.fromstring(stdin.read(), i8, sep=' ')
    N = pin[0]
    M = pin[1]
    L = pin[2]
    ABC = pin[3: M * 3 + 3].reshape((-1, 3))
    A = ABC[:, 0] - 1
    B = ABC[:, 1] - 1
    C = ABC[:, 2]
    Q = pin[M * 3 + 3]
    st = (pin[M * 3 + 4: 2 * Q + M * 3 + 4] - 1).reshape((-1, 2))

    graph = csr_matrix((C, (A, B)), shape=(N, N))
    dist = np.array(floyd_warshall(graph, directed=False))
    dist[dist > L + 0.5] = 0
    dist[dist > 0] = 1
    min_dist = np.array(floyd_warshall(dist))
    min_dist[min_dist == np.inf] = 0
    for i in range(st.shape[0]):
        print(int(min_dist[st[i, 0], st[i, 1]] - 1.0))


if __name__ == '__main__':
    main()
