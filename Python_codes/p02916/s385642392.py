N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
U=list(map(int,input().split()))

goukei=0

before=1000
for i in range(N):
    goukei+=T[S[i]-1]
    if before+1==S[i]:
        goukei+=U[S[i]-2]
    
    before=S[i]
    
print(goukei)