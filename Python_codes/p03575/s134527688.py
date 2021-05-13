def main():
    from collections import defaultdict,deque
    N,M = map(int,input().split())
    AB = []
    for _ in range(M):
        a,b = map(int,input().split())
        AB.append((a-1,b-1))
    ans = M
    for i in range(M):
        s,g = AB[i]

        edge = defaultdict(list)
        for j in range(M):
            if i == j:
                continue
            a,b = AB[j]
            edge[a].append(b)
            edge[b].append(a)

        visited = [False]*N
        targets = deque([s])
        while targets:
            t = targets.popleft()
            visited[t] = True
            for dest in edge[t]:
                if visited[dest]:
                    continue
                if dest == g:
                    ans -= 1
                    break
                targets.append(dest)
            else:
                continue
            break
    print(ans)
        
        







main()