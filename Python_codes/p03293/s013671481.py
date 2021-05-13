import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = input()
T = input()
leng = len(S)
for i in range(leng+1):
    S = S[-1]+S[:-1]
    if S==T:
        print('Yes')
        break
else:
    print('No')