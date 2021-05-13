import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
N = len(S)

print(sum(S[i] != S[i+1] for i in range(N-1)))
