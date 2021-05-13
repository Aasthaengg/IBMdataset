N=int(input())

#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
S = [[0 for j in range(2)] for i in range(N)]

for i in range(N):
    A,B=map(int,input().split())
    B=int(B)
    S[i][0]=A
    S[i][1]=B


T=sorted(S,key=lambda x:x[1])
goukei=0

for i in range(N):
    simekiri=T[i][1]
    goukei+=T[i][0]
    if goukei>simekiri:
        print("No")
        exit()
print("Yes")