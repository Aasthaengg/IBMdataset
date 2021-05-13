n, k = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9+7

ans = 0
for i in range(n-1):
    count=0
    for j in range(i+1, n):
        if A[i]>A[j]:
            count+=1
    ans = (ans + (count*((k*(k+1))//2)%mod))%mod

for i in range(n-1):
    count=0
    for j in range(i+1, n):
        if A[i]<A[j]:
            count+=1
    ans = (ans + (count*((k*(k-1))//2)%mod))%mod
print(ans)