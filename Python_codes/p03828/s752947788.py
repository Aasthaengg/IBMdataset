def f(n):
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
n=int(input())
ans=[1 for i in range(n+1)]
mod=10**9+7
tmp=1
for i in range(2,n+1):
    t=f(i)
    for j,k in t:
        ans[j]+=k
for i in range(n+1):
    tmp=tmp*ans[i]%mod
print(tmp)