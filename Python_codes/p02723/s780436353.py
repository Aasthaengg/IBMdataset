import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = input()
if S[2]==S[3] and S[4]==S[5]:
    print('Yes')
else:
    print('No')