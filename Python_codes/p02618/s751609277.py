import numpy as np
import sys
read = sys.stdin.read
 

D = int(input())
CS = np.array(read().split(), np.int32)
C = CS[:26]
S = CS[26:].reshape((-1, 26))
del CS
 
last = np.zeros((26, ))


def getContestType_at_d(d, k):
    s = -10000000
    for i in range(26):
        mask = np.ones((26, ))
        mask[i] = 0
        #ps = S[d][i] - np.sum(C * (d + 1 - last) * mask)
        score =S[d][i] - np.sum(C * (min(365, d + k) + 1 - last))
        if s < score:
            s = score
            t = i
 
    last[t] = d + 1
 
    return t + 1, s


#score = 0
#pscore = 0
ans = []
for d in range(D):
    t, s = getContestType_at_d(d, 10)
    ans.append(t)
    #ans.append(getContestType_at_d(d, k))
    #score += s
    #pscore += ps

#print('pscore:', pscore)
#print('score:', score)

 
print('\n'.join(map(str, ans)))