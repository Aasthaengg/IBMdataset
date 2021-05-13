n=int(input())

def fact(n):
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

from collections import defaultdict
d = defaultdict(int)
for i in range(1,n):
    num=i+1
    for div in fact(num):
        d[div[0]]+=div[1]

ans=1
for a in d.values():
    ans*=(a+1)
    ans%=(10**9+7)
ans%=(10**9+7)
print(ans)