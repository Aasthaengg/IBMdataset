import sys
read = sys.stdin.read
from itertools import permutations
def main():
    def warshall_floyd(d):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d
 
    n, m, r = map(int, input().split())
    rs = tuple(map(int, input().split()))
    d = [[10**9] * n for _ in range(n)]
    m = map(int, read().split())
    mmm = zip(m, m, m)
    for s, t, dis in mmm:
        s -= 1
        t -= 1
        d[t][s] = d[s][t] = dis
    for j1 in range(n):
        d[j1][j1] = 0
    res = warshall_floyd(d)
    rsp = tuple(permutations(rs))
    result = float('inf')
    for rspe in rsp:
        res_t = 0
        for i1 in range(r - 1):
            res_t += res[rspe[i1]-1][rspe[i1+1]-1]
        result = min(result, res_t)
    print(result)
 
if __name__ == '__main__':
    main()