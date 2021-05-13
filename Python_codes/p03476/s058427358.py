import math

#素数判定
def IsPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

q = int(input())

a = [0] * (10**5 + 1)

for i in range(10**5 + 1):
    #条件を満たすなら1
    if IsPrime(i) and IsPrime((i + 1) / 2) and i % 2 == 1:
        a[i] = 1
    else:
        a[i] = 0

#先頭からの累積和をとる
for i in range(10**5):
    a[i + 1] += a[i]

#クエリ処理
for i in range(q):
    l, r = map(int, input().split())
    print(a[r] - a[l - 1])