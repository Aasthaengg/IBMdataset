N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=pow(10,9)+7
answer=0
for n in range(N-1):
    number=A[n]
    for n_ in range(n,N-1):
        if A[n_+1]<number:
            answer+=1
sort_A=sorted(A,reverse=True)
answer2=0
for n in range(N-1):
    number=sort_A[n]
    for n_ in range(n,N-1):
        if sort_A[n_+1]<number:
            answer2+=1
print((answer*K+answer2*(K-1)*K//2)%mod)
