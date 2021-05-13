def main():
    n,m = map(int,input().split())
    lines = [[] for _ in range(n)]
    for i in range(m):
        l,r,d = map(int,input().split())
        lines[l-1].append([r-1,d])
        lines[r-1].append([l-1,-d])

    from collections import deque
    # from heapq imort heappush, heappop
    inf = 10**18
    dist = [inf]*n

    for i in range(n):
        if dist[i] != inf:
            continue
        dist[i] = 0
        q = deque()
        q.append([i,0])
        while q:
            now,cnt = q.popleft()
            for nxt,nd in lines[now]:
                if dist[nxt] == inf:
                    dist[nxt] = cnt+nd
                    q.append([nxt,cnt+nd])
                    continue
                if dist[nxt] != cnt+nd:
                    print('No')
                    return 0
    print('Yes')

if __name__ == '__main__':
    main()

