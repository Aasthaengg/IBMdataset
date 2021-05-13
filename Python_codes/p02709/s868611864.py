import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

A2=[(num,ind) for ind,num in enumerate(A)]
A2.sort(reverse=True)

L=[0]*N

for i in range(N):
    num,ind=A2[i]
    NL=[0]*N
    for j in range(i+1):
        right=N-1-(i-j)
        NL[j]=max(NL[j],abs(right-ind)*num+L[j])

        if j!=N-1:
            NL[j+1]=max(NL[j+1],abs(j-ind)*num+L[j])
    L=NL
print(max(L))