n = int(input())
a = list(map(int,input().split()))
ans = 1
p = [0,0,0]  
mod = 10**9+7
for i in range(n):
    q = 0
    for j in range(3):
        if p[j] == a[i]:
            q +=1
    for k in range(3):
        if p[k] == a[i]:
            p[k] += 1
            break
    ans = ans*q%mod
print(ans%mod)