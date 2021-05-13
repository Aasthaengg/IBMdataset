from collections import deque


n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


def d(s):
    ret = [10 ** 18] * n
    ret[s] = 0
    q = deque()
    q.append(s)
    while len(q):
        now = q.popleft()
        for to in g[now]:
            if ret[to] < 10 ** 18:
                continue
            ret[to] = ret[now] + 1
            q.append(to)
    return ret


# print(d(n-1))

fennec = d(0)
snuke = d(n - 1)
cnt = 0
for i in range(n):
    if fennec[i] <= snuke[i]:
        cnt += 1
    else:
        cnt -= 1
if cnt > 0:
    print("Fennec")
else:
    print("Snuke")
