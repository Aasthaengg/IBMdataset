N,M=map(int,input().split())
A=[input() for _ in range(N)]
B=[input() for _ in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        cnt=0
        for k in range(M):
            if A[i+k][j:j+M]==B[k]:
                cnt+=1
        if cnt==M:
            print("Yes")
            exit()
print("No")