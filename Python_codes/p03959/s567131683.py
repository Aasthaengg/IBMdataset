N=int(input())
T=list(map(int,input().split()))
A=list(map(int,input().split()))
cand=[-1]*N
cand2=[-1]*N
flag=1
ans=1
p=10**9+7
for i in range(N):
    if i==0:
        cand[i]=T[i]
    else:
        if T[i]!=T[i-1]:
            cand[i]=T[i]
for i in range(N-1,-1,-1):
    if i==N-1:
        cand2[i]=A[i]
    else:
        if A[i]!=A[i+1]:
            cand2[i]=A[i]
#print(cand)
#print(cand2)

ans=1
for i in range(N):
    if (cand[i]==-1)and(cand2[i]==-1):
        ans=(ans*min(T[i],A[i]))%p
    elif (cand[i]==-1):
        if T[i]<cand2[i]:
            ans=0
    elif (cand2[i]==-1):
        if A[i]<cand[i]:
            ans=0
    else:
        if cand[i]!=cand2[i]:
            ans=0
print(ans)


#print(flag,cand)
"""
lmax=[0]*N
rmax=[0]*N
for i in range(N):
    if i==0:
        lmax[i]=cand[i]
        rmax[N-1-i]=cand[N-1-i]
    else:
        if cand[i]==-1:
            lmax[i]=lmax[i-1]
        else:
            lmax[i]=cand[i]

        if cand[N-i-1]==-1:
            rmax[N-i-1]=rmax[N-i]
        else:
            rmax[N-i-1]=cand[N-i-1]
#print(lmax,rmax)
for i in range(N):
    if cand[i]==-1:
        ans=(ans*min(A[i],T[i]))%p
if flag==0:
    print("0")
else:
    print(ans%p)
"""