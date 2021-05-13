import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,K = LI()
S = LS2()

S[K-1] = S[K-1].lower()

print(''.join(S))