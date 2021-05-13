import fractions
N,M=map(int,input().split())
S=input()
T=input()
lcm=(N*M)/fractions.gcd(N,M)
num=0
s=[]
t=[]
flag=1
sindex=0
tindex=0
while (sindex<N)and(tindex<M):
    if S[sindex]!=T[tindex]:
        flag=0
        break
    sindex=sindex+(N//fractions.gcd(N,M))
    tindex = tindex + (M // fractions.gcd(N, M))
"""
for j in range(N):
    s.append([S[j],int(1+(num//N)*j)-1])
for j in range(M):
    t.append([T[j], int(1 + (num // M) * j) - 1])
#print(s,t)
while (sindex<N)and(tindex<M):
    #print(sindex,tindex)
    if s[sindex][1]==t[tindex][1]:
        if s[sindex][0]!=t[tindex][0]:
            flag=0
            break
        sindex=sindex+1
        tindex=tindex+1
    elif s[sindex][1]<t[tindex][1]:
        sindex=sindex+1
    else:
        tindex = tindex + 1
    #input()
"""
if flag==0:
    print("-1")
else:
    print(int(lcm))


