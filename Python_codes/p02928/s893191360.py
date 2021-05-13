n,k = map(int,input().split())
L = list(map(int,input().split()))
mod = 10**9 +7

cnt = 0
for i in range(n-1):
    tmp = 0
    for j in range(i+1,n):
        if L[i] > L[j]:
            cnt +=1
cnt2 = 0
li = []
for i in range(n):
    tmp = 0
    for j in range(n):
        if L[i] > L[j]:
            cnt2 +=1

ans = cnt*k%mod
ans += cnt2*k*(k-1)//2%mod
print((ans)%mod)
