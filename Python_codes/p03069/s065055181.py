N=int(input())
S=input()
b=[None]*(N+1)
b[0]=0
w=[None]*(N+1)
w[N]=0
for i in range(1,N+1):
    b[i]=b[i-1]+(S[i-1]=='#')
for i in range(N-1,-1,-1):
    w[i]=w[i+1]+(S[i]=='.')
print(min([x+y for x,y in zip(b,w)]))