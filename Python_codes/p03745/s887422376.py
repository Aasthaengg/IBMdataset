N=int(input())
A=list(map(int,input().split()))
pumi=0
ff=0
cut=1
for i in range(0,N-1):
    if pumi==0:
        ff=0
    elif pumi==-1:
        ff=-1
    elif pumi==1:
        ff=1

    if A[i+1]>A[i]:
        pumi=1
    elif A[i+1]<A[i]:
        pumi=-1

    if pumi==-1 and ff==1:
        cut+=1
        pumi=0
    elif pumi==1 and ff==-1:
        cut+=1
        pumi=0
print(cut)