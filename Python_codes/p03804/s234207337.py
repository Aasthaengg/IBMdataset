N,M = map(int,input().split())
A = [input().strip() for _ in range(N)]
B = [input().strip() for _ in range(M)]
ind = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        flag = 0
        for k in range(M):
            for l in range(M):
                if B[k][l]!=A[i+k][j+l]:
                    flag = 1
                    break
            if flag==1:break
        if flag==0:
            ind = 1
            break
    if ind==1:break
if ind==1:
    print("Yes")
else:
    print("No")