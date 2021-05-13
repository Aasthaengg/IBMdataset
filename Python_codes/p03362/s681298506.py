

# 素数生成器
def generate_primes():
    from collections import defaultdict
    from itertools import count
    D = defaultdict(list)

    q = 2
    for q in count(2):
        if q in D:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]
        else:
            yield q
            D[q*q].append(q)

N = int(input())
res = []
cnt = 0
for p in generate_primes():
    if p % 5 == 1:
        cnt += 1
        res.append(p)
    if cnt >= N:
        break

print(*res)