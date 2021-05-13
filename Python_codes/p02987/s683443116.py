import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
if S[0] == S[1] == S[2] == S[3]:
    print('No')
elif S[0] == S[1] and S[2] == S[3]:
    print('Yes')
elif S[0] == S[2] and S[1] == S[3]:
    print('Yes')
elif S[0] == S[3] and S[1] == S[2]:
    print('Yes')
else:
    print('No')
