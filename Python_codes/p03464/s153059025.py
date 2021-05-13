def resolve():
    # from collections import deque
    k = int(input())
    a = list(map(int, input().split()))
    rl = [2, 2]
    ra = a[::-1]

    for i in range(k):
        nxt = []
        nowa = ra[i]
        if (rl[-1] // nowa) - ((rl[0]-1)//nowa) > 0:
            nxt.append((((rl[0]-1)//nowa)+1)*nowa)
            nxt.append((rl[-1]//nowa)*nowa + nowa-1)
        if not nxt:
            print(-1)
            exit()
        rl = nxt

    print("{} {}".format(rl[0], rl[-1]))
resolve()