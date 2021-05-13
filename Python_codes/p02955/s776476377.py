N, K = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)

def divisor(n):
    res = []
    rn = int(n**0.5) + 1 
    for i in range(1, rn):
        if n % i == 0:
            res.append(i)
            if i != n / i:
                res.append(int(n / i))
    return sorted(res)

Y = divisor(S)

ans = 1
for i in range(len(Y)-1, 0, -1):
    cnt = []
    for j in range(N):
        cnt.append(A[j] % Y[i])

    cnt = sorted(cnt)

    cnt_s = [0]
    tmp = 0
    for j in range(N):
        tmp += cnt[j]
        cnt_s.append(tmp)
    minc = 10**10
    for j in range(N+1):
        M = cnt_s[j]
        P = (N-j)*Y[i] - (cnt_s[N]-cnt_s[j])
        minc = min(max(M,P),minc)
    if minc <= K:
        ans = Y[i]
        break

print(ans)