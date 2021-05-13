N,K=map(int,input().split())
S=input()
Happy=0
for i in range(N):
    if i>0 and S[i-1]==S[i]=='L':
        Happy+=1
    elif i<N-1 and S[i]==S[i+1]=='R':
        Happy+=1
print(min(Happy+2*K,N-1))