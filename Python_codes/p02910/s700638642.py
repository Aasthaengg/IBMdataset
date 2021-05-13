import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
N = len(S)
S1 = S[::2]
S2 = S[1::2]

r = sum(s in ['R','U','D'] for s in S1) + sum(s in ['L','U','D'] for s in S2)
print('Yes' if r == N else 'No')
