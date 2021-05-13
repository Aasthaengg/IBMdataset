from bisect import bisect_right as br

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

ans=0
Bc=[]
for i in range(N):
    Bc.append(N-br(C,B[i]))

S=[sum(Bc)]
for j in range(N):
    S.append(S[j]-Bc[j])

for a in A:
    b=br(B,a)
    ans+=S[b]
print(ans)
