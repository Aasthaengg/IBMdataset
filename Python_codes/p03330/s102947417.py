
if __name__ == '__main__':
    N,C=list(map(int,input().split()))
    D=[list(map(int,input().split())) for i in range(C)]
    c=[list(map(int,input().split())) for i in range(N)]

    mode={0:{i:0 for i in range(C)},1:{i:0 for i in range(C)},2:{i:0 for i in range(C)}}

    for i in range(N):
        for j in range(N):
            mode[(i+j+2)%3][c[i][j]-1]+=1

    ans=1e10

    for i in range(C):
        for j in range(C):
            if i!=j:
                for k in range(C):
                    if i!=k and j!=k:
                        temp=0
                        for l in range(C):
                            temp+=D[l][i]*mode[0][l]
                            temp+=D[l][j]*mode[1][l]
                            temp+=D[l][k]*mode[2][l]
                        ans=min(ans,temp)

    print(ans)
