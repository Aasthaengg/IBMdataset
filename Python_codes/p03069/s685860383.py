N=int(input())
S=input()
Wcum=[0]*(N+1)
Bcum=[0]*(N+1)
for i in range(N):
    Wcum[i+1]=Wcum[i]+(S[i]=='.')
    Bcum[i+1]=Bcum[i]+(S[i]=='#')
ans=N
for i in range(N+1):
    ans=min(ans,(i-Wcum[i])+(N-i-(Bcum[N]-Bcum[i])))
print(ans)