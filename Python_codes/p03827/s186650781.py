N=int(input())
S=input()

M=0
X=0
for s in S:
    if s=="I":
        X+=1
        M=max(M,X)
    else:
        X-=1
print(M)
