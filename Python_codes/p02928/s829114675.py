mod = 10**9 + 7
n,k = map(int,input().split())
A = list(map(int,input().split()))
# その数より右にあるもの
ans = 0
for i in range(n):
    migi = 0
    a = A[i]
    for j in range(i+1,n):
        if a > A[j]:
            migi += 1
    ans += migi * k
    ans %= mod
# 全体で、その数よりも小さいもの(ループするので)
for i in range(n):
    zen = 0
    a = A[i]
    for j in range(n):
        if a > A[j]:
            zen += 1
    # 等差数列のやつ 初項は0, 項数はk,末項はzen * (k-1)
    ans += ((zen*(k-1) * k //2)%mod)
    ans %= mod
print(ans)
