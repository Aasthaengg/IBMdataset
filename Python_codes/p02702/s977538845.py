S=[int(i) for i in list(input())][::-1]
R={}
def dic_add(x):
    if x in R:
        R[x]+=1
    else:
        R[x]=1
def dic_check(x):
    if x in R:
        return R[x]
    else:
        return 0
def pow_k(x,n,p=10**9+7):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2!=0:
            K=(K*x)%p
        x=(x*x)%p
        n//=2
    return (K*x)%p
N=len(S)
r=0
res=0
for i in range(N):
    r=(S[i]*pow_k(10,i,2019)+r)%2019
    if not r:
        res+=1
    res+=dic_check(r)
    dic_add(r)
print(res)