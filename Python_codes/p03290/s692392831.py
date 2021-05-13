D,G = map(int, input().split())
pc = [list(map(int,input().split())) for _ in range(D)]

ans = 1 << 29
t = []
for bit in range(1<<D):
    score = 0
    f = 0
    # フラグが立ってる問題を全完
    for i in range(D):
        if bit & (1<<i):
            score += pc[i][0]*100*(i+1) + pc[i][1]
            f += pc[i][0]
            if score >= G: break
    # 全完した問題以外の中から点数の高い順に解いていく
    nokori = []
    for j in range(D):
        if not (bit & (1<<j)):
            nokori.append(pc[j] + [j+1])
    nokori = list(reversed(nokori))
    for d in nokori:
        for x in range(d[0]):
            if score >= G: break
            score += 100*(d[2])
            f += 1
        if score >= G: break
    ans = min(ans,f)
print(ans)
