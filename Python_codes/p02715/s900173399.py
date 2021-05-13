# coding: utf-8
N, K = list(map(int, input().split()))
mod = 10 ** 9 + 7
sum = 0
count = [0 for _ in range(K+1)]
pows = [0 for _ in range(K+1)]

def cal_pow(k, pows):
    if pows[k] == 0:
        pows[k] = pow(k,N, mod)
        return pows[k]
    else:
        return pows[k]

for h in range(K):
    k = K-h
    sub, alpha = 0,2
    while True:
        if alpha*k <= K:
            sub += count[alpha*k]
            alpha += 1
        else:break
    count[k] = (cal_pow(K//k, pows) - sub) % mod

for k, c in enumerate(count):
    sum += k * c % mod
print(sum % mod)