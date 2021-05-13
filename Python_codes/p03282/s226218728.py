# ABC106-C

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

S = LI2()
K = I()

for i in range(K):
    if S[i] != 1:
        print(S[i])
        break
    elif i == K-1 and S[i] == 1:
        print(1)
