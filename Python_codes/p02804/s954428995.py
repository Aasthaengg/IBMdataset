n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
num=[1]
M=10**9+7
for i in range(n):
    x=(num[i]*(i+1))%M
    num.append(x)
def inverse(number,mod):
    m=mod-2
    mod2=""
    while m!=0:
        if m%2==0:
            mod2="0"+mod2
        else:
            mod2="1"+mod2
        m=m//2
    two=[]
    for i in range(len(mod2)):
        if mod2[len(mod2)-1-i]=="1":
            two.append(i)
    ret=1
    for i in two:
        v=i
        retsub=number
        while v>0:
            retsub=retsub**2
            retsub=retsub%mod
            v-=1
        ret*=retsub
    ret=ret%mod
    return ret
def comb(p,q):
    ret1=num[p]
    ret2=inverse(num[p-q],M)
    ret3=inverse(num[q],M)
    ret=(ret1*ret2*ret3)%M
    return ret
#min
minsum=0
for i in range(n):
    if n-(i+1)>=k-1:
        minsum+=(a[i] * comb(n-i-1,k-1))%M
        minsum%=M
b=sorted(a,reverse=True)
#max
maxsum=0
for i in range(n):
    if n-(i+1)>=k-1:
        maxsum+=(b[i] * comb(n-i-1,k-1))%M
        maxsum%=M
print((maxsum-minsum)%M)
