N,K=map(int,input().split())
A=list(map(int,input().split()))

H=(K*(K-1))//2

X=0
M=10**9+7
I=(M+1)//2

for i in range(N):
    P,Q,S,V=0,0,0,0
    for j in range(N):
        if A[i]<A[j]:
            P+=1
            if j<i:
                S+=1
        if A[i]>A[j]:
            Q+=1
            if i<j:
                V+=1
    X+=K*(S+V)+H*(P+Q)
    X%=M
print((X*I)%M)