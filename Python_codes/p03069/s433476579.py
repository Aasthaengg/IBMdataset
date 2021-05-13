N=int(input())
S=input()
B=[]
W=[]
i=0
while i<N:
    if S[i]=='#':
        B.append(i)
    else:
        W.append(i)
    i+=1

X=len(B)
Y=len(W)
ans=0
i=j=0
while i<X and j<Y:
    if B[i]<W[j]:
        i+=1
        j+=1
        ans+=1
    else:
        j+=1
print(ans)