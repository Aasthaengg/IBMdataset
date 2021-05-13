
import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
inp = sys.stdin.buffer.readline
def inpS(): return inp().rstrip().decode()
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
INF = 1<<60
# A：想定する最短距離と計算(WF)で算出した最短距離が合っているか判定
# A[i][j] > A[i][k] + A[k][j] : -1
# AとWFが合っていたら最短距離の和を出力
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

def resolve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    csr = csr_matrix(np.array(A))
    wf =  floyd_warshall(csr, directed=False)
    for i in range(N):
        wf[i][i] = INF
        A[i][i] = INF
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] != wf[i][j]:
                print(-1)
                return
            if wf[i][j] < np.min(wf[i] + wf[j]):
                ans += wf[i][j]
    print(int(ans//2))

if __name__ == "__main__":
    resolve()