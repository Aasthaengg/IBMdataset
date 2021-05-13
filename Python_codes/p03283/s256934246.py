def main():
    N,M,Q=map(int,input().split())
    p=[[0 for i in range(509)] for j in range(509)]

    for i in range(1,M+1):
        L,R=map(int,input().split())
        p[L][R]+=1
    for i in range(1,N+1):
        for j in range(1,N+1):
            p[i][j]+=p[i][j-1]
    for i in range(1,N+1):
        for j in range(1,N+1):
            p[i][j]+=p[i-1][j]
    for i in range(1,Q+1):
        L,R=map(int,input().split())
        print(p[R][R]+p[L-1][L-1]-p[L-1][R]-p[R][L-1])

main()
