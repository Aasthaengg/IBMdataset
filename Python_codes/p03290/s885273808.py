D,G = map(int,input().split())
PC = [tuple(map(int,input().split())) for i in range(D)]

ans = 9999
for b in range(1<<D):
    sc = pr = 0
    for i,(p,c) in enumerate(PC):
        if b&(1<<i):
            sc += c + (i+1)*100*p
            pr += p
    if sc >= G:
        ans = min(ans, pr)
        continue
    remsc = G - sc
    for i,(p,_) in reversed(list(enumerate(PC))):
        if b&(1<<i): continue
        for j in range(p):
            remsc -= (i+1)*100
            pr += 1
            if remsc <= 0:
                ans = min(ans, pr)
                break
        else:
            continue
        break
    if remsc <= 0:
        ans = min(ans, pr)
print(ans)