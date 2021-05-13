N,M=map(int,input().split())
A=[input()for i in range(N)]
B=[input()for i in range(M)]
for i in range(N-M+1):
    for j in range(len(A[0])-len(B[0])+1):
        l=[]
        for k in range(M):
            l.append(A[i+k][j:j+M])
        if l==B:print('Yes');exit()
print('No')