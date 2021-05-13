from collections import deque

N, M, Q = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(Q)]

def calc(li):
    score = 0
    for a, b, c, d in l:
        if li[b-1]-li[a-1] == c:
            score += d
    return score

que = deque([[i] for i in range(1, M+1)])
ans = 0

while que:
    li = que.popleft()
    if len(li) == N:
        score = calc(li)
        ans = max(ans, score)
    else:
        for i in range(li[-1],M+1):
            next = li + [i]
            que.append(next)
    #print(que)

print(ans)
