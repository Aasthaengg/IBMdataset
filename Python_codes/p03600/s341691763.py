import sys
import copy
import heapq
from collections import deque

# sys.setrecursionlimit(100001)
INF = sys.maxsize


# ===CODE===
def main():
    n = int(input())
    dist_mat = []
    for i in range(n):
        l = list(map(int, input().split()))
        dist_mat.append(l)

    dist_mat_calc = [[INF for i in range(n)] for j in range(n)]

    ans = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist_mat_calc[i][j] = min(dist_mat_calc[i][j], dist_mat[i][k] + dist_mat[k][j])

    tmp = [[dist_mat_calc[j][i] if dist_mat_calc[j][i] != INF else 0 for i in range(n)] for j in range(n)]
    if tmp != dist_mat:
        print(-1)
        exit(0)

    ans = 0

    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            tmp = min([x+y for (x,y) in zip(dist_mat_calc[i], dist_mat_calc[j])])
            if dist_mat_calc[i][j] < tmp:
                ans+=dist_mat_calc[i][j]

    print(ans)





if __name__ == '__main__':
    main()
