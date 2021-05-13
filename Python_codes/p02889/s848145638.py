def main():
    import sys
    input = sys.stdin.readline
    n,m,l = map(int,input().split())
    E = [[float("INF")]*n for i in range(n)]
    for i in range(m):
        a,b,c = map(int,input().split())
        E[a-1][b-1] = c
        E[b-1][a-1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                E[i][j] = min(E[i][j],E[i][k]+E[k][j])
    wa = [[float("INF")]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if E[i][j] <= l:
                wa[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                wa[i][j] = min(wa[i][j],wa[i][k]+wa[k][j])
    
    x = int(input())
    for i in range(x):
        s,g = map(int,input().split())
        if wa[s-1][g-1] == float("INF"):
            print(-1)
        else:
            print(wa[s-1][g-1]-1)

    
if __name__ == "__main__":
    main()