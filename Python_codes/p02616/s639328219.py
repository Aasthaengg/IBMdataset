mod = 1000000007
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
ans = 1
# 選択の余地がない時
if len(A) == K:
    for i in range(K):
        ans = ans * (A[i]%mod) % mod
# 負になってしまう時
elif A[-1] < 0 and K%2 == 1:
    for i in range(K):
        ans = ans * (A[-i-1]%mod) % mod
else:
    n = 0
    p = -1
    # Kが奇数の時、正の候補の最大値をあらかじめ消費しておき、偶数の時と同様に処理できるようにする。
    if K%2 == 1:
        ans = ans * (A[p]%mod) % mod
        p -= 1
    # 正/負の候補から２つずつ消費していく
    for _ in range(K//2):
        if A[n]*A[n+1] > A[p]*A[p-1]:
            ans = ans * (A[n]%mod) % mod
            ans = ans * (A[n+1]%mod) % mod
            n += 2
        else:
            ans = ans * (A[p]%mod) % mod
            ans = ans * (A[p-1]%mod) % mod
            p -= 2        

print(ans)