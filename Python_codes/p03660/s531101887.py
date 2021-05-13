def resolve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    adjlist = {}
    for a, b in AB:
        adjlist.setdefault(a-1, [])
        adjlist.setdefault(b-1, [])
        adjlist[a-1].append(b-1)
        adjlist[b-1].append(a-1)
    import collections
    q = collections.deque([0])
    sources = [None for _ in range(N)]
    sources[0] = -1
    while q:
        v = q.popleft()
        for nxt in adjlist[v]:
            if sources[nxt] is None:
                sources[nxt] = v
                q.append(nxt)
    
    # print(adjlist)
    # print(sources)
    shortest = [N-1]
    cur = N-1
    while True:
        shortest.append(sources[cur])
        if sources[cur] == 0:
            break
        cur = sources[cur]
    shortest.reverse()
    # print(shortest)
    shortest = collections.deque(shortest[1:-1])

    b_nexts = set(adjlist[0])
    b_nexts.discard(N-1)
    w_nexts = set(adjlist[N-1])
    w_nexts.discard(0)

    colored = [False for _ in range(N)]
    colored[0] = True
    colored[N-1] = True
    b_turn = True
    while True:
        # print(colored)
        # print(b_nexts)
        # print(w_nexts)
        # print(shortest)
        if b_turn:
            if len(b_nexts) == 0:
                print("Snuke")
                return
            if len(shortest) > 0:
                nxt = shortest.popleft()
                b_nexts.remove(nxt)
            else:
                nxt = b_nexts.pop()
            if nxt in w_nexts:
                w_nexts.remove(nxt)
        else:
            if len(w_nexts) == 0:
                print("Fennec")
                return
            if len(shortest) > 0:
                nxt = shortest.pop()
                w_nexts.remove(nxt)
            else:
                nxt = w_nexts.pop()
            if nxt in b_nexts:
                b_nexts.remove(nxt)
        # print(nxt)
        colored[nxt] = True
        for v in adjlist[nxt]:
            if colored[v] is False:
                if b_turn:
                    b_nexts.add(v)
                else:
                    w_nexts.add(v)
        
        b_turn = not b_turn
    #print("Snuke" if b_turn else "Fennec")


if '__main__' == __name__:
    resolve()