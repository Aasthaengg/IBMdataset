
def combination_table(N):
    C=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i):
            if j==0 or j==i:
                C[i][j]=1
            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    return C[2:]

if __name__ == '__main__':
    N,A,B=list(map(int,input().split()))
    V=list(map(int,input().split()))
    V.sort(reverse=True)
    temp=V[:A]
    max_mean=sum(temp)/A
    count=0
    C=combination_table(N+2)

    if V[0]!=V[A-1]:
        temp_1=V.count(V[A-1])
        temp_2=V[:A].count(V[A-1])
        count+=C[temp_1-1][temp_2]
        """temp_1=V.count(V[0])
        temp_2=V[:A].count(V[0])
        count+=C[temp_1-1][temp_2]"""
    elif V[0]==V[A-1]:
        for i in range(A,B+1):
            temp_1=V.count(V[0])
            count+=C[temp_1-1][i]

    print(max_mean)
    print(count)
