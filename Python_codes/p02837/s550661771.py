N = int(input())
A = [0]*N
X = [0]*N
Y = [0]*N
for i in range(N):
    A[i] = int(input())
    Xsmall = [0]*A[i]
    Ysmall = [0]*A[i]
    for j in range(A[i]):
        Xsmall[j],Ysmall[j] = map(int,input().split())
    X[i] =Xsmall
    Y[i] = Ysmall

opinions = []
for i in range(N):
    opinion = [-1]*N
    for j in range(A[i]):
        if Y[i][j] == 0:
            opinion[X[i][j]-1] = 0
        elif Y[i][j] == 1:
            opinion[X[i][j]-1] = 1
    opinions.append(opinion)
answer = 0


for i in range(2**N):
    check = 0
    count = 0
    
    for j in range(N):
        if ((i >> (N-j-1)) & 1) == 1:
            count += 1
            for k in range(A[j]):
                num = X[j][k]
                if ((i >> (N-num)) & 1) == Y[j][k]:
                    
                    continue
                else:
                    check = -1
                    break
            
    
    if check == 0:
        answer = max(answer,count)
    
    
print(answer)