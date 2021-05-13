from collections import Counter

MOD = 10 ** 9 + 7


def factorization(n):
    arr = dict()
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt

    if temp != 1:
        arr[temp] = 1

    if not arr and n != 1:
        arr[n] = 1

    return arr


ct = Counter()
for i in range(2, int(input()) + 1):
    ct.update(factorization(i))

ans = 1
for t in ct.values():
    ans = (ans * (t + 1)) % MOD
print(ans)
