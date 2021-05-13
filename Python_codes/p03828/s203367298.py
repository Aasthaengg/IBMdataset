from collections import defaultdict

n=int(input())
mod=10**9+7
d=defaultdict(int)

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

    for i in range(len(arr)):
        d[arr[i][0]]+=arr[i][1]
    return

ans=1
for i in range(1,n+1):
    factorization(i)

for i,m in d.items():
    if i!=1:
        ans*=(m+1)
        ans%=mod
print(ans)