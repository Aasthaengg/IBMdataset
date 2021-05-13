from collections import deque
H, W = map(int, input().split())
S = [input() + "#" for _ in range(H)]
S.append("#" * (W + 1))

todo = deque()
done = set()
ans = 0
for sh in range(H):
    for sw in range(W):
        if S[sh][sw] == "#":
            continue
        s = (sh, sw)
        done.clear()
        done.add(s)
        todo.append((s, 0))
        while todo:
            p, count = todo.popleft()
            ncount = count + 1
            for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nh, nw = p[0] + dh, p[1] + dw
                if S[nh][nw] == "#":
                    continue
                np = (nh, nw)
                if np in done:
                    continue
                done.add(np)
                ans = max(ans, ncount)
                todo.append((np, ncount))
print(ans)