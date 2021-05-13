# from pprint import pprint
# import math
# import collections

# n = int(input())
a, b = map(int, input().split(' '))


# a = list(map(int, input().split(' ')))

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.55 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


fact_a = set([f[0] for f in factorization(a)])
fact_b = set([f[0] for f in factorization(b)])

ans = fact_a & fact_b
ans.add(1)

# print(fact_a, fact_b)
print(len(ans))
