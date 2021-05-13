# 累積和(2次元)を用いた解法
from itertools import accumulate
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N,M,Q,*lr = map(int, read().split())

    LR = [[0]*(N+1) for _ in range(N+1)]
    query = []
    for i, (l, r) in enumerate(zip(*[iter(lr)]*2)):
        if i < M:
            LR[l][r] += 1
        else:
            query.append((l, r))
    
    for i in range(1,N+1):
        LR[1][i] += LR[1][i-1]
        LR[i][1] += LR[i-1][1]
    
    for i in range(2, N+1):
        for j in range(2,N+1):
            LR[i][j] += LR[i-1][j] + LR[i][j-1] - LR[i-1][j-1]
    
    for p, q in query:
        ans = LR[q][q] - LR[p-1][q] - LR[q][p-1] + LR[p-1][p-1]
        print(ans)


if __name__ == "__main__":
    main()
