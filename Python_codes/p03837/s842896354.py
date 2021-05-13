def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(i!=j):
                    d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
def main():

    n,m=map(int, input().split())
    edge = [[] for _ in range(n)]
    d = [[float("inf")]*n for i in range(n)]
    d_1 = [[float("inf")]*n for i in range(n)]
    e_lis = [0]*m
    for i in range(m):
        a,b,c=map(int, input().split())
        d[a-1][b-1]=d[b-1][a-1]=d_1[a-1][b-1]=d_1[b-1][a-1]=c
    res = warshall_floyd(d,n)
    cnt=0
    for i in range(n):
        for j in range(n):
            if(res[i][j]!=d_1[i][j] and d_1[i][j]<10000):
                cnt+=1
    print(cnt//2)


if __name__ == '__main__':
    main()
