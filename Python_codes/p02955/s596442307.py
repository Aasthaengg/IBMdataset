# https://atcoder.jp/contests/abc136/submissions/6708242

def solve():
    n, k = map(int, input().split())
    a = tuple(sorted(map(int, input().split()), reverse=True))

    sum_a = sum(a)
    e = set()
    divisor = 1
    while divisor * divisor <= sum_a:
        if sum_a % divisor == 0:
            e.add(divisor)
            e.add(sum_a // divisor)
        divisor += 1

    e = sorted(e, reverse=True)
    # 約数降順

    for cand in e:
        r = tuple(sorted(x % cand for x in a if x % cand != 0))

        accm = [0]
        t = 0
        for x in r:
            t += x
            accm.append(t)

        accp = [0]
        t = 0
        for x in r:
            t += cand - x
            accp.append(t)

        m = len(r)
        for i in range(m + 1):
            if (accm[i] == (accp[m] - accp[i])) and (accm[i] <= k):
                return cand
    return -1


print(solve())

# 操作で総和は不変
