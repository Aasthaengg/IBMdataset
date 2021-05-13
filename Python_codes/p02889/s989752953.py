#juppy's code for testing run time only. 
def main():
    import sys
    input = sys.stdin.readline
    n,m,l = map(int,input().split())
    d = [[10**12]*n for _ in [0]*n]
    for i in range(m):
        a,b,c = map(int,input().split())
        if l >= c:
            d[a-1][b-1] = d[b-1][a-1] = c
    for i in range(n):
        d[i][i] = 0
 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
 
    edge = [[10**12]*n for _ in [0]*n]
    for i in range(n):
        for j in range(n):
            if d[i][j] <= l:
                edge[i][j] = 1
 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                edge[i][j] = min(edge[i][j],edge[i][k] + edge[k][j])
 
    q = int(input())
    for _ in [0]*q:
        s,t = map(int,input().split())
        if edge[s-1][t-1] >= 10**12:
            print(-1)
        else:
            print(edge[s-1][t-1]-1)
 
if __name__ == '__main__':
    main()