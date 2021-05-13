import sys

def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = LS2()
S1 = [S[i] for i in range(N//2)]
S2 = [S[i] for i in range(N//2,N)]

if S1 == S2:
    print('Yes')
else:
    print('No')