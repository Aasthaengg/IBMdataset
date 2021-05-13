N=int(input())
T=list(map(int,input().split()))
A=list(map(int,input().split()))
Tr,Ar=[0]*N,[0]*N

ct,ca=0,0
for i in range(N):
    if T[i] > ct:
        ct=T[i]
        Tr[i]=[ct,ct]
    else:
        Tr[i]=[1,ct]

    if A[N-1-i] > ca:
        ca=A[N-1-i]
        Ar[N-1-i]=[ca,ca]
    else:
        Ar[N-1-i]=[1,ca]

MOD=1000000007
ans=1
for tr,ar in zip(Tr,Ar):
    l = max(tr[0],ar[0])
    r = min(tr[1],ar[1])
    if r<l:
        print(0)
        exit()
    ans = (ans*(r-l+1))%MOD
print(ans)
