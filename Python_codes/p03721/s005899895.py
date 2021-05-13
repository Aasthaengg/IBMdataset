N,K=map(int,input().split())

#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
S = [[0 for j in range(2)] for i in range(100010)]

for i in range(N):
    T=list(map(int,input().split()))
    S[T[0]][0]=T[0]
    S[T[0]][1]+=T[1]

#print(S)

for i in range(100010):
    if S[i][0]!=0:
        K-=S[i][1]
        if K<=0:
            print(S[i][0])
            exit()
