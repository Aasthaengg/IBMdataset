N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = int(1e9) + 7


def wa(n, a):
    return ((n*(n+1))//2 * a) % MOD


ans = 0
# 内部の転倒数
for n in range(N):
    # 内部
    a = 0
    nA = A[n+1:]
    t = A[n]
    for na in nA:
        if t > na:
            a += 1
    temp = wa(K, a)
    ans += temp
    ans = ans % MOD

    # 外部
    b = 0
    nA = A[:n+1]
    for na in nA:
        if t > na:
            b += 1
    temp = (b * K*(K-1)//2)%MOD
    ans += temp
    ans = ans % MOD

print(ans)
