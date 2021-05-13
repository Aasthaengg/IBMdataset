import sys, itertools
input = sys.stdin.readline

def main():

    # d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
    def warshall_floyd(d, V):
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        return d # d[i][j]に頂点i, j間の最短距離を格納

    n,m,r = map(int,input().split())
    R = list(map(int,input().split()))
    for i in range(r):
        R[i] -= 1

    d = [[10**10] * n for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        d[a-1][b-1] = c
        d[b-1][a-1] = c

    d = warshall_floyd(d, n)
    ans = 10**10

    ptr = list(itertools.permutations(R, len(R))) # 順列列挙 5P3
    for i in ptr:
        tmp = 0
        for j in range(len(i)-1):
            tmp += d[i[j]][i[j+1]]
        ans = min(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()
