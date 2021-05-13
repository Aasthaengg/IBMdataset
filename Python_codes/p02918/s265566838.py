N,K=map(int,input().split())
S=str(input())



happiness=N
for i in range(N):
    if i==0:
        if S[0]=='L':
            happiness-=1
            continue
    if i==N-1:
        if S[N-1]=='R':
            happiness-=1
            continue
    if S[i]=='R':
        if S[i+1]=='L':
            happiness-=1
    else:
        if S[i-1]=='R':
            happiness-=1

print(min(happiness+2*K,N-1))