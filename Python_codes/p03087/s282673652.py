N,Q=map(int,input().split())
S=input()
l=0
r=0

s=[]
s.append(0)

for i in range(1,N):
    if(S[i-1]=='A' and S[i]=='C'):

        s.append(s[i-1]+1)

    else:
        s.append(s[i-1])

for i in range(Q):

    l,r=map(int,input().split())

    print(s[r-1]-s[l-1])
