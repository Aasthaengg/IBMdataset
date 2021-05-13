H,W,K = map(int,input().split())

import itertools
from collections import defaultdict
ZO = [0,1]

CHOCO = []
for i in range(H):
    s = input()
    CHOCO.append(s)

ans = 10**16
C = 0

for i in itertools.product(ZO,repeat = H-1):
    saki = 0
    To = defaultdict(int)
    To[0] = saki
    for j in range(H-1):
        if i[j]==0:
            To[j+1] = saki
        else:
            saki += 1
            To[j+1] = saki
    tmpans = saki
    #print(To,tmpans)
    NowWhite = [0]*(saki+1)
    preW = 0
    for w in range(W):
        h = 0
        while 1:
            C+= 1
            #print(NowWhite,h)
            #if C>10000:
              #break
            if CHOCO[h][w] == '1':
                NowWhite[To[h]] += 1
                if NowWhite[To[h]] > K:
                    #print('break')
                    tmpans += 1
                    NowWhite = [0]*(saki+1)
                    h = -1
                    if preW==w:
                        tmpans += 10**16
                        break
                    preW = w
            if h==H-1:
                #print('h==H-1')
                break
            h += 1
    ans = min(ans,tmpans)
print(ans)