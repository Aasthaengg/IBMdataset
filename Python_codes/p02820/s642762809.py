N,K = map(int,input().split())
R,S,P = map(int,input().split())
D={"r":P,"s":R,"p":S}
T = input().strip()
A = {i:[] for i in range(K)}
for i in range(N):
    A[i%K].append(T[i])
cnt = 0
for k in range(K):
    if len(A[k])>0:
        cnt += D[A[k][0]]
        for i in range(1,len(A[k])):
            if A[k][i]==A[k][i-1]:
                A[k][i] = 0
            elif A[k][i]!=A[k][i-1]:
                cnt += D[A[k][i]]
print(cnt)