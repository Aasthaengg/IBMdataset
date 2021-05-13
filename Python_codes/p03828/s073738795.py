from collections import Counter


def factorization(n):
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] += cnt

    if temp != 1:
        arr[temp] += 1

    if len(arr.keys()) == 0 and n != 1:
        arr[n] += 1


N = int(input())
arr = Counter()
for i in range(1, N + 1):
    factorization(i)

cnt = 1
MOD = 10 ** 9 + 7
for v in list(arr.values()):
    cnt *= (v + 1)
    cnt %= MOD

print(cnt)
