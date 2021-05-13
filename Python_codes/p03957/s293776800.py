import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
c_ok = False
for s in S:
    if s=='C':
        c_ok = True
    if s=='F' and c_ok:
        print('Yes')
        break
else:
    print('No')