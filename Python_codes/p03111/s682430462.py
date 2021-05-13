import sys
input=sys.stdin.readline

n,a,b,c=map(int,input().split())
L=[]
A=[a,b,c]
for i in range(n):
    L.append(int(input()))
L.sort()

ans=10**9
for i in range(4**n):
    F=[[] for i in range(3)] #竹格納:[A,B,C]
    now=i
    for j in range(n):
        r=now%(4**(j+1))
        chk=r//(4**(j))
        if chk!=3:
            F[chk].append(L[j])
        now-=r    
    if F[0] and F[1] and F[2]: #竹が1本以上あるとき
        mp=0
        for k in range(3):
            f=F[k]
            mp+=abs(sum(f)-A[k])+10*(max(0,len(f)-1))
        ans=min(mp,ans)
print(ans)