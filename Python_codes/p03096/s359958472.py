import sys

N=int(input())
C=[int(input()) for i in range(N)]
mod=10**9+7

if N==1:
    print(1)
    sys.exit()

S=[C[0]]

for i in range(1,N):
    if C[i]!=C[i-1]:
        S.append(C[i])

L=len(S)

if L==1:
    print(1)
    sys.exit()

AL=[[] for i in range(2*10**5+1)]

for i in range(L):
    AL[S[i]].append(i)

PLUS=[0]*(2*10**5+1)

NOW=1

for i in range(L):
    NOW,PLUS[S[i]]=(NOW+PLUS[S[i]])%mod,(PLUS[S[i]]+NOW)%mod
    #PLUS[S[i]]+=NOW
    

    #print(NOW,PLUS)

#print(PLUS)
print(NOW)
    
    
