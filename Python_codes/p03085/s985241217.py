import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

b = input()
if b=='A':
    print('T')
elif b=='T':
    print('A')
elif b=='C':
    print('G')
else:
    print('C')