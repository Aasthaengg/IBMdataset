from collections import deque
if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        v, k, *tmp = map(int, input().split())
        for j in range(len(tmp)):
            tmp[j] -= 1
        graph.append(tmp)
    visited = [False] * n
    qu = deque()
    qu.appendleft((0, 0))
    ans = [-1] * n
    visited[0] = True

    while qu:
        now, dis = qu.pop()
        ans[now] = dis

        for nei in graph[now]:
            if not visited[nei]:
                visited[nei] = True
                qu.appendleft((nei, dis + 1))
    for i in range(n):
        print(i+1,ans[i])    
