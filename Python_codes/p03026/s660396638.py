import queue
def main():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    c = list(map(int, input().split()))
    c.sort(reverse=True)
    ans = [None]*n
    a = [i for i in range(n)]
    a.sort(key=lambda x: len(g[x]), reverse=True)
    f = [True]*n
    f[a[0]] = False
    q = queue.Queue()
    q.put(a[0])
    ans[a[0]] = c[0]
    x = 1
    while not q.empty():
        target = q.get()
        for v in g[target]:
            if f[v]:
                f[v] = False
                ans[v] = c[x]
                q.put(v)
                x += 1
    score = 0
    f = [True]*n
    f[0] = False
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        target = q.get()
        for v in g[target]:
            if f[v]:
                f[v] = False
                score += min(ans[target], ans[v])
                q.put(v)
    print(score)
    for i in range(n):
        print(ans[i], end="")
        if i < n-1:
            print(" ",end="")
        else:
            print("")

if __name__ == "__main__":
    main()
