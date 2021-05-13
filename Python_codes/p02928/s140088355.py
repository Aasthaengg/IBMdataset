n, k =map(int,input().split())
a = list(map(int,input().split()))
ans = 0
u = 1000000007
for i in range(n):
    p = a[i]
    l = 0
    r = 0
    for j in range(i+1,n):
        if p > a[j]:
            r += 1
    ans += r*k*(k+1)//2
    ans %= u
    for g in range(0,i):
        if p > a[g]:
            l += 1
    ans += l*k*(k-1)//2
    ans %= u
print(int(ans))