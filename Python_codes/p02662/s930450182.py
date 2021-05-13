N, S = map(int, input().split())

*A, = map(int, input().split())

mod = 998244353

sumT = [0]*6005
sumT[0] = 1
sumT[A[0]] = 1

for a in A[1:]:
    for j in range(3001):
        sumT[j] *= 2

    for j in range(3000, -1, -1):
        sumT[j+a] += sumT[j] // 2
        sumT[j+a] %= mod
        sumT[j] %= mod

    sumT[0] += 1
    sumT[0] %= mod

    sumT[a] += 1
    sumT[a] %= mod


print(sumT[S] % mod)
