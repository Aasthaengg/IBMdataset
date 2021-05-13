def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
ans=1
mod=10**9+7
from collections import defaultdict
d=defaultdict(int)
n=int(input())
for i in range(2,n+1):
    lst=factorization(i)
    for a,b in lst:
        d[a]+=b
for v in d.values():
    ans*=(v+1)
    ans%=mod
print(ans)