N = int(input())
P = []
for _ in range(N):
    x, y, h = map(int, input().split())
    P.append((x, y, h))

found = False
for i in range(len(P)):
    x, y, h = P[i]
    for cy in range(101):
        for cx in range(101):
            H = h + abs(x - cx) + abs(y - cy)
            if all(h == max(H - abs(x - cx) - abs(y - cy), 0) for x, y, h in P):
                print(cx, cy, H)
                found = True
                break
        if found:
            break
    if found:
        break