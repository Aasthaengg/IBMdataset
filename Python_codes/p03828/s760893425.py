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

MOD=10**9+7

n=int(input())
li=[0]*2000

for i in range(1,n+1):
    c=factorization(i)
    #print(c)
    for j in range(len(c)):
        li[c[j][0]]+=c[j][1]

ans=1

for i in range(2,n+1):
    ans=ans*(li[i]+1)
    ans=ans%MOD

print(ans)
