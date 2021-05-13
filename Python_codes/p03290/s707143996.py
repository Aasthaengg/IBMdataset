D,G = map(int,input().split())
pc = [list(map(int,input().split())) for i in range(D)]
ans = float('inf')
for bit in range(1<<D):
    _sum = 0
    _ans = 0
    rest = [i for i in range(D)]
    for i in range(D):
        if bit & (1<<i):
            _sum += pc[i][0]*(i+1)*100 + pc[i][1]
            _ans += pc[i][0]
            rest.remove(i)
    if _sum < G and len(rest) != 0:
        i = max(rest)
        for j in range(pc[i][0]-1):
            _sum += (i+1)*100
            _ans += 1
            if _sum >= G:
                break
    if _sum >= G:
        ans = min(ans,_ans)
print(ans)