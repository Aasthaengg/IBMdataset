N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(N)]
CD = [tuple(map(int,input().split())) for i in range(M)]
for a,b in AB:
    best_i = -1
    best_d = 10**9
    for i,(c,d) in enumerate(CD):
        dist = abs(a-c) + abs(b-d)
        if dist < best_d:
            best_d = dist
            best_i = i
    print(best_i + 1)