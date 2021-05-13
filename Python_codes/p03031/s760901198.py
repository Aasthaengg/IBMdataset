#!/usr/bin/env python

# input
n, m = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
k = [t[i][0] for i in range(m)]
s = [t[i][1:] for i in range(m)]

# calc
# bit full search
ans = 0 
for i in range(2**n):
    tmp = i 
    sw = []
    if i == 0:
        sw = [0] 
    while tmp > 0:
        sw.append(tmp&1)
        tmp = tmp>>1
    while len(sw) < n:
        sw.append(0)

    #print('sw =', sw)
    
    # check whether current sw satisfies the condision.
    ok = True
    # light bulb j
    for j in range(m):
        tmp = 0 
        for a in range(k[j]):
            tmp += sw[s[j][a]-1]
        if tmp%2 != p[j]:
            ok = False
            break
    if ok: 
        # print('sw =', sw)
        ans += 1

print(ans)
