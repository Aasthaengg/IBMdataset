import heapq
from collections import deque


def max_value(V, N, K, A, B):
    V = deque(V.copy())
    value = 0
    neg_que = list()
    for _ in range(A):
        if len(V) == 0:
            break
        v = V.popleft()
        value += v
        if v < 0:
            heapq.heappush(neg_que, v)
    for _ in range(B):
        if len(V) == 0:
            break
        v = V.pop()
        value += v
        if v < 0:
            heapq.heappush(neg_que, v)
    max_throw_num = max([K - min([N, A + B]), 0])
    for _ in range(max_throw_num):
        if len(neg_que) == 0:
            break
        v = heapq.heappop(neg_que)
        value -= v
    return value


def main():
    N, K = list(map(int, input().split(' ')))
    V = list(map(int, input().split(' ')))
    max_v = 0
    for a in range(K + 1):
        for b in range(K + 1):
            if a + b > K:
                continue
            v = max_value(V, N, K, a, b)
            max_v = max([v, max_v])
    print(max_v)


if __name__ == '__main__':
    main()
