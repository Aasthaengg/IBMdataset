# coding: utf-8
import sys
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 持っている宝石をDに詰めるのは最後
N, K = lr()
V = lr()
answer = 0
V = V[::-1] + V[::-1]
for x in range(K+1):
    # x回Dから取り出す、K-x回戻すことが可能
    x = min(x, N)
    for i in range(N-1, N-1+x+1):
        take = V[i-x+1:i+1]
        take.sort(reverse=True)
        result = sum(take)
        if result > answer:
            answer = result
        for j in range(K-x):
            if take:
                result -= take.pop()
                if result > answer:
                    answer = result

print(answer)
