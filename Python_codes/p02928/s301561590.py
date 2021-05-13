MOD = 10**9 + 7

n,k = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
ans2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if i < j and a[i] > a[j]:
                ans += 1
            if i > j and a[i] > a[j]:
                ans2 += 1
            
mal = k*(k+1)//2 % MOD
mal2 = k*(k-1)//2 % MOD
print((ans * mal % MOD + ans2 * mal2 % MOD) % MOD)