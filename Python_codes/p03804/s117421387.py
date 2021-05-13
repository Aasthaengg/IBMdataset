N,M = map(int,input().split())
A = []
for _ in range(N):
    A.append(input().strip())
B = []
for _ in range(M):
    B.append(input().strip())
flag = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        ind = 0
        for k in range(M):
            for l in range(M):
                if A[i+k][j+l]!=B[k][l]:
                    ind = 1
                    break
            if ind==1:break
        if ind==0:
            flag = 1
    if flag==1:break
if flag==1:
    print("Yes")
else:
    print("No")