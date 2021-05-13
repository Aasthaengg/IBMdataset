import itertools
n, c = map(int, input().split())
cs = [[0]*(10**5+10) for _ in range(c+1)]
#cs = [[0]*(15) for _ in range(c+1)]
for i in range(n):
    s, t, ch = map(int, input().split())
    s += 1
    t += 1
    cs[ch][t] = s

for i in range(1,c+1):
    for j in range(1,10**5+10):
    #for j in range(15):
        if cs[i][cs[i][j]] != 0:
            start = cs[i][j]
            cs[i][j] = cs[i][start]
            cs[i][start] = 0

#print(cs)
rsw = [0]*(10**5+10)
#rsw = [0]*(15)
for i in range(1,c+1):
    for j in range(1,10**5+10):
    #for j in range(15):
        if cs[i][j] != 0:
            cs[i][j] -= 1
            rsw[cs[i][j]] += 1
            rsw[j] -= 1

print(max(itertools.accumulate(rsw)))