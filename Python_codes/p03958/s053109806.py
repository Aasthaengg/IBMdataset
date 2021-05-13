# -*- coding: utf-8 -*-
K, T = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
A = [(-a, i) for i, a in enumerate(A)]

import heapq
heapq.heapify(A)

prev = -1
while len(A) > 1:
    a, i = heapq.heappop(A)
    if i == prev:
        b, j = heapq.heappop(A)
        prev = j

        heapq.heappush(A, (a, i))
        b += 1
        if b != 0:
            heapq.heappush(A, (b, j))

    else:
        prev = i
        a += 1
        if a != 0:
            heapq.heappush(A, (a, i))



print(- A[0][0] - 1)





