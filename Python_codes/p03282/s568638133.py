import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし

S = LI2()
K = I()

for i in range(K):
    if i == K-1 or S[i] != 1:
        print(S[i])
        break
else:
    print(1)