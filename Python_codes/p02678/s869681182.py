import queue

def main():
    n, m = map(int, input().split())
    graph = [[]for i in range(n + 1)]
    a = None
    b = None
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    sign = [0 for i in range(n + 1)]
    vis = [False for i in range(n + 1)]
    q = queue.Queue(0)
    q.put(1)
    vis[1] = True
    while q.empty() == False:
        u = q.get()
        for val in graph[u]:
            if vis[val] == False:
                vis[val] = True
                q.put(val)
                sign[val] = u
    for i in range(2, n + 1):
        if sign[i] == 0:
            print("No")
            return
    print("Yes")
    for i in range(2, n + 1):
        print(sign[i])



if __name__ == "__main__":
    main()
