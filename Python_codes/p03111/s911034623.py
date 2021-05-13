# coding: utf-8
import sys
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# Nは最大8まで、Aに使う竹はどれ？
N, A, B, C = lr()
bamboo = [ir() for _ in range(N)]
answer = 10 ** 5
for pattern in itertools.product(range(4), repeat=N):
    use = [0] * 3
    mp = 0
    for p, bam in zip(pattern, bamboo):
        if p == 3:
            continue
        if use[p] != 0:
            mp += 10
        use[p] += bam
    if use.count(0) != 0:
        continue
    mp += abs(A-use[0]) + abs(B-use[1]) + abs(C-use[2])
    if mp < answer:
        answer = mp

print(answer)
# 23