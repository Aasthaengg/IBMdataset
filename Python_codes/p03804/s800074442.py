N,M=map(int,input().split())
A=[input() for i in range(N)]
B=[input() for i in range(M)]

ans="No"
for j in range(N-M+1):
    for i in range(N-M+1):
        isMatch=True
        for y in range(M):
            for x in range(M):
                if A[j+y][i+x]!=B[y][x]:
                    isMatch=False
                    
        if isMatch:
            ans="Yes"
            break        

print(ans)