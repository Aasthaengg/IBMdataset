import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())+['END']
lis = []
now = S[0]
for s in S[1:]:
    if s!=now:
        lis.append(now)
        now = s

print(len(lis)-1)