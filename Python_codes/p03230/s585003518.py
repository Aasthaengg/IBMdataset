N = int(input())
k = int((2*N)**0.5)+1
if 2*N==k*(k-1):
    print("Yes")
    A = [[0 for _ in range(k+1)] for _ in range(k+1)]
    cnt = 1
    for i in range(1,k):
        for j in range(i+1,k+1):
            A[i][j] = cnt
            A[j][i] = A[i][j]
            cnt += 1
    S = [[] for _ in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,k+1):
            if i!=j:
                S[i].append(A[i][j])
    print(k)
    for i in range(1,k+1):
        print(k-1,*S[i])
else:
    print("No")