L=list(map(int,input()))
n=len(L)
def power(a,n):
    x=1
    L=list(format(n,'b'))
    l=len(L)
    for i in range(l):
        if int(L[l-i-1])==1:        
            x=(x*a)%(10**9+7)
        a=(a*a)%(10**9+7)
    return x
X=power(3,n-1)%(10**9+7)
count=1
for i in range(1,n):
    if L[i]==1:
        k=n-i-1
        count+=1
        X+=(power(3,k)%(10**9+7))*(power(2,count-1)%(10**9+7))
X+=power(2,count)%(10**9+7)
print(X%(10**9+7))
