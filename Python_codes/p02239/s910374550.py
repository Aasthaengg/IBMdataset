from collections import deque
def MAIN():
    n = int(input())
    li = [[] for _ in range(n + 1)]
    ans = [[i, -1] for i in range(n + 1)]
    ans[1][1] = 0
    for _ in range(n):
        u, k, *v = map(int, input().split())
        li[u] = v
    dp = deque([1])
    while dp:
        u = dp.popleft()
        for v in li[u]:
            if ans[v][1] == -1:
                ans[v][1] = ans[u][1] + 1
                dp.append(v)
    for d in ans[1:]:
        print(*d)
MAIN()

