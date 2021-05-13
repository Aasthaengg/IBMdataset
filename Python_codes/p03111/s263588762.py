n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]

from collections import deque

ans = float('inf')

def dfs(i, abc, cost):
    global ans
    stack = deque([[i, abc, cost]])
    while stack:
        i, abc, cost = stack.pop()
        a, b, c = abc
        if i == n:
            if a * b * c:
                ans = min(ans, abs(A-a) + abs(B-b) + abs(C-c) + cost*10)
            continue
        for e in (0, 1, 2, 3):
            n_cost = cost
            n_abc = abc[:]
            if e < 3:
                if abc[e]:
                    n_cost += 1
                n_abc[e] += l[i]
            stack.append([i + 1, n_abc, n_cost])

dfs(0, [0,0,0], 0)

print(ans)