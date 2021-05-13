from random import random, randint

K = 26
d = int(input())

c = list(map(int, input().split()))

s = []
for i in range(d):
    q = list(map(int, input().split()))
    s.append(q)

ans = []
last = [-1 for i in range(K)]
for i in range(d):
    x = []
    for j in range(K):
        x.append(pow(s[i][j] * c[j] * (i - last[j]), 3))

    sum = 0
    for j in range(K):
        sum += x[j]

    for j in range(K):
        x[j] /= sum

    prob = random()
    cur = 0
    for j in range(K):
        if cur + x[j] <= prob:
            cur += x[j]
            continue
        ans.append(j)
        last[j] = i
        break


def get_result():
    res = 0
    last = [-1 for i in range(K)]
    for i in range(d):
        res += s[i][ans[i]]
        last[ans[i]] = i
        for j in range(K):
            res -= c[j] * (i - last[j])
    return res


# print(get_result())
for qq in range(100):
    i = randint(0, d - 1)
    nw = randint(0, K - 1)

    old = ans[i]
    old_res = get_result()

    ans[i] = nw
    res = get_result()

    if res < old_res:
        ans[i] = old

    # print(get_result())

for u in ans:
    print(u + 1)