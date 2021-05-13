import sys

def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()

S[3] = '8'

print("".join(S))