from itertools import product
N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
INF = 10 ** 9
t1 = set([0,1,2,3])
t2= set([1,2,3])
def calc(t):
    t3 = set(t)
    if not (t3 == t1 or t3 == t2): return INF
    a, b, c = 0, 0, 0
    cnt = 0
    for i, v in enumerate(t):
        if v != 0: cnt += 1
        if v == 1: a += l[i]
        elif v == 2: b += l[i]
        elif v == 3: c += l[i]
    return abs(a-A) + abs(b-B) + abs(c-C) + (cnt-3) * 10

ans = 10 ** 9
# 4進数の配列を生成する
# 0:未使用,1:aに使用,2:bに使用,3:cに使用
for p in product(range(4), repeat=N):
    ans = min(ans, calc(p))

print(ans)

