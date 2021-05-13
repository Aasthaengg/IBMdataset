N,T,*ABf = map(int, open(0).read().split())
AB = [ABf[i:i+2] for i in range(0, len(ABf), 2)]
AB.sort()
dp = [[0] * 2 for _ in range(6000)]
filled = set([0])
for x in AB:
    temp = set()
    change = []
    for y in filled:
        if y + x[0] <= (T-1) + max(dp[y][1],x[0]):
            if dp[y+x[0]][0] <= dp[y][0] + x[1]:
                change.append((y,y+x[0],dp[y][0]+x[1],x[0]))
    for y in change:
        if dp[y[1]][0] == y[2]:
            dp[y[1]][1] = y[3]
        else:    
            dp[y[1]][0] = y[2]
            dp[y[1]][1] = y[3]
            temp.add(y[0]+x[0])
    filled = filled | temp
print(max(dp)[0])