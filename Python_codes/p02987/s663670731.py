import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
S.sort()
if S[0]==S[1] and S[1]!=S[2] and S[2]==S[3]:
    print('Yes')
else:
    print('No')