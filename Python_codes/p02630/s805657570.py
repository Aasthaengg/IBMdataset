n=int(input())
A=list(map(int,input().split()))

asum = sum(A)
S={}
for i in range(len(A)):
    if A[i] in S:
        S[A[i]]+=1
    else:
        S[A[i]]=1

D=[]
q=int(input())
for i in range(q):
    diff=0
    b,c =map(int,input().split())
    if not c in S:
        S[c]=0
    if b in S:
        diff = (S[b]*c-S[b]*b)
        S[c]+=S[b]
        S[b]=0

    asum+=diff
    D.append(asum)

for d in D:
    print(d)


