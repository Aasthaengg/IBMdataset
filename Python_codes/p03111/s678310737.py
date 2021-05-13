n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = float("INF")
for a in range(2**n):
    d0 = [(a >> b) & 1 for b in range(n)]
    for c in range(2**n):
        d1 = [(c >> d) & 1 for d in range(n)]
        abc = [0] * 3
        ans_ = 0
        for i in range(n):
            if d0[i] == 1 and d1[i] == 1:
                if abc[0]: ans_ += 10
                abc[0] += l[i]
            elif d0[i] == 0 and d1[i] == 1:
                if abc[1]: ans_ += 10
                abc[1] += l[i]
            elif d0[i] == 1 and d1[i] == 0:
                if abc[2]: ans_ += 10
                abc[2] += l[i]
        if abc[0] == 0 or abc[1] == 0 or abc[2] == 0: continue
        ans_ += abs(abc[0]-A)+abs(abc[1]-B)+abs(abc[2]-C)
        ans = min(ans, ans_)
print(ans)