def bfs(fd, n):
    visited = set()
    ans = 1
    for i in range(1, n + 1):
        if i in visited: continue
        volume = 1
        queue = fd[i]
        visited.add(i)
        while queue:
            x = queue.pop()
            if x in visited: continue
            visited.add(x)
            volume += 1
            queue |= fd[x]
        ans = max(ans, volume)
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())
    fd = {i+1:set() for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        fd[a].add(b)
        fd[b].add(a)
    print(bfs(fd, n))