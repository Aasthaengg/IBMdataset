N, K = map(int, input().split())
A = list(map(int, input().split()))
MAX = max(len(bin(K))-2, len(bin(max(A)))-2)
bK = bin(K)[2:].zfill(MAX)
degs = [0]*MAX # 2^iの位に１を持つ数の個数
for i in range(N):
    b = bin(A[i])[2:].zfill(MAX)
    for d in range(MAX):
        if b[d] == "1":
            degs[d] += 1

tot = 0
dp = [0]*MAX # dp[i]: 上からiケタ目が1でかつ初めて許した場合
for f in range(MAX):
    t = 2 ** (MAX-1)
    ans = 0
    is_free = 0
    for i in range(MAX):
        d = degs[i]
        if i == f:
            if bK[i] == "1":
                is_free = 1
        elif i < f:
            if bK[i] == "1":
                d = max(d, N-d)
        elif i > f and is_free:
            d = max(d, N-d)
        ans += t * d
        t //= 2
    tot = max(tot, ans)
t = 2 ** (MAX-1)
ans = 0
for i in range(MAX):
    d = degs[i]
    if bK[i] == "1":
        d = max(d, N-d)
    ans += t*d
    t //= 2
tot = max(tot, ans)    
print(tot)