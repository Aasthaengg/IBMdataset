
def minMP(length,LIST):
    k=len(LIST)
    LONG=[]
    if k==0:
        return -1
    for i in range(1,2**k):
        long=0
        cnt=-1
        for j in range(k):
            mod=i%2
            if mod==1:
                long+=LIST[j]
                cnt+=1
            i//=2
        LONG.append([long,10*cnt])
    
    ans=float("inf")
    for ll,mp in LONG:
        ans=min(ans,mp+abs(ll-length))
    return ans 

N,a,b,c=map(int,input().split())
L=[]
Ans=float("inf")
for i in range(N):
    l=int(input())
    L.append(l)

for n in range(3**N):
    L_A=[];L_B=[];L_C=[]
    for i in range(N):
        mod=n%3
        n//=3
        if mod==0:
            L_A.append(L[i])
        elif mod==1:
            L_B.append(L[i])
        else:
            L_C.append(L[i])
    MP_A=minMP(a,L_A)
    MP_B=minMP(b,L_B)
    MP_C=minMP(c,L_C)
    
    if MP_A==-1 or MP_B==-1 or MP_C==-1:
        continue
    else:
        Ans=min(Ans,MP_A+MP_B+MP_C)

print(Ans)