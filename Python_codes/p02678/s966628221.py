import collections

def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)

    check = [0]*(n+1)
    ans = [0]*(n+1)
    q = collections.deque()
    q.append(1)
    check[1] = 1

    while len(q) != 0:
        v = q.popleft()
        for u in g[v]:
            #print(u)
            if check[u] == 0:
                check[u] = 1
                ans[u] = v
                q.append(u)

    for i in range(2,n+1):
        if ans[i] == 0:
            print('No')
            return

    print('Yes')
    for i in range(2,n+1):
        print(ans[i])

main()
