N=int(input())
S=input()

E=[0]*N
W=[0]*N

if S[0]=='E':
    E[0]=1
else:
    W[0]=1

i=1
while i<N:
    if S[i]=='E':
        E[i]=E[i-1]+1
        W[i]=W[i-1]
    else:
        W[i]=W[i-1]+1
        E[i]=E[i-1]
    i+=1

E=[0]+E
W=[0]+W

ans=N
j=1
while j<=N:
    count=W[j-1]+(E[N]-E[j])
    ans=min(ans,count)
    j+=1

print(ans)