import math


def eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


q = int(input())
l, r = [], []
for _ in range(q):
    _lr = list(map(int, input().split()))
    l.append(_lr[0])
    r.append(_lr[1])
N = 10 ** 5 + 1

prime_list = eratosthenes(N)
prime_flag = [False for _ in range(10 ** 5 + 2)]
like_2017 = [0 for _ in range(10 ** 5 + 2)]
like_cnt = 0

for p in prime_list:
    prime_flag[p] = True

for i in range(10 ** 5 + 2):
    if prime_flag[(i + 1) // 2] and prime_flag[i]:
        like_cnt += 1
    like_2017[i] = like_cnt

for i in range(q):
    print(like_2017[r[i]] - like_2017[l[i] - 1])
