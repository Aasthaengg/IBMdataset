n,k = map(int,input().split())
a_L = list(map(int,input().split()))

mod = 10**9+7
ans = 0
for i in range(n):
    x,y = 0,0
    for j in range(i):
        if a_L[i] > a_L[j]:
            x += 1
    for j in range(n):
        if a_L[i] > a_L[j]:
            y+=1
    ans += y*((1+k)*k//2) - x*k
    ans = ans%mod

print(ans)