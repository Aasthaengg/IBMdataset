N,Q=map(int,input().split())
S=input()
l=0
r=0
l=[0]*Q
r=[0]*Q
s=[]
s.append(0)

for i in range(1,N):
    if(S[i-1]=='A' and S[i]=='C'):

        s.append(s[i-1]+1)

    else:
        s.append(s[i-1])

for i in range(Q):

    l[i],r[i]=map(int,input().split())
for i in range(Q):
    print(s[r[i]-1]-s[l[i]-1])

