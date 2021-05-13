n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9 + 7

ans = 0
for i in range(n):
    c_0 = 0
    c_1 = 0
    for j in range(n):
        if i == j:
            pass
        elif a[i] > a[j]:
            if i < j:
                c_1 += 1
            else:
                c_0 += 1      
    ans += c_1*k*(k+1)//2 + c_0*k*(k-1)//2
    ans %= mod
print(ans)