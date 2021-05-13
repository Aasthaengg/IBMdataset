def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from collections import Counter
N, K = MI()
add = Counter([])

for _ in range(N):
    a, b = MI()
    tmp = add[a]
    add[a] = b
    add[a] += tmp

num = sorted(list(add.keys()))
cnt = 0

for n in num:
    cnt += add[n]
    if cnt >= K:
        print(n)
        break