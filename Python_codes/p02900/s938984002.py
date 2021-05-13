def factorize(N):
    if N == 1: return {1:1}
    res = {}
    for i in range(2, N):
        if i**2 > N: break
        if N % i != 0: continue
        num = 0
        while N % i == 0:
            N = int(N/i)
            num += 1
        res[i] = num
    if N>1: res[N] = 1
    return res

A, B = map(int, input().split())
resA = factorize(A)
resB = factorize(B)
res = set(resA.keys()) & set(resB.keys())
ans = len(res) if 1 in res else len(res)+1
print(ans)