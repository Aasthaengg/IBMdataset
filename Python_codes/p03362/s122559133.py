n = int(input())

def primes(n):
    primes = [1] * (n+1)
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not primes[i] :
            continue
        for j in range(i * 2, n + 1, i):
            primes[j] = 0

    for i in range(len(primes)):
        if i %5 != 1:
            primes[i] = 0
    return primes

# n<= 55555
primes_list = primes(55556)
# 考え方
# 以下のような。5で割ってあまりが1になるような素数だけを出力しておく
# [11, 31, 41, 61, 71, 101,...]
# ここからどの5つをとっても、5で割れば割り切れるので、条件を満たすことができる

ans = []
for i in range(len(primes_list)):
    if primes_list[i]:
        ans.append(i)
        if len(ans) == n:
            break
ans = map(str, ans)
print(" ".join(ans))