import copy
def warshall_floyd(d):
    cnt = 0
    d_first = copy.deepcopy(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    for i in range(len(d)):
        for fir, rev in zip(d_first[i], d[i]):
            if (rev < fir) and fir != float('inf'):
                cnt += 1
    return cnt//2

if __name__ == '__main__':
    n,w = map(int,input().split()) #n:頂点数　w:辺の数

    d = [[float("inf")]*n for i in range(n)] 
    for i in range(w):
        x,y,z = map(int,input().split())
        d[x-1][y-1] = z
        d[y-1][x-1] = z
    for i in range(n):
        d[i][i] = 0 #自身のところに行くコストは０
    print(warshall_floyd(d))
