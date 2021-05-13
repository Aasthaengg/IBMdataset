from collections import deque


def main():
    n = int(input())
    ans = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    c = list(map(int, input().split()))
    c.sort(reverse=True)
    root = 0
    max_deg = 0
    for i in range(n):
        if max_deg < len(graph[i]):
            root = i
            max_deg = len(graph[i])
    q = deque([root])
    ans[root] = c[0]
    idx = 1
    while q:
        now_v = q.pop()
        for next_v in graph[now_v]:
            if ans[next_v] == 0:
                ans[next_v] = c[idx]
                idx += 1
                q.append(next_v)
    print(sum(c[1:]))
    print(" ".join(map(str, ans)))


if __name__ == '__main__':
    main()
