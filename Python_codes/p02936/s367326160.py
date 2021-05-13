def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n, q = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        adj[a].append(b)
        adj[b].append(a)
    ans = [0]*n
    for _ in range(q):
        p, x = map(int, input().split())
        p -=1
        ans[p] += x
    
    from collections import deque
    que = deque([0])
    parent = [-1]*n
    while que:
        node = que.pop()
        for v in adj[node]:
            if v == parent[node]:
                continue
            parent[v] = node
            que.append(v)
            ans[v] += ans[node]
    for a in ans:
        print(a)

        

    
if __name__ == '__main__':
    main()