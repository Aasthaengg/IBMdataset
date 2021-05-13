import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, V = mapint()
B, W = mapint()
T = int(input())

if A==B:
    print('YES')
else:
    if V<=W:
        print('NO')
    else:
        if (V-W)*T>=abs(A-B):
            print('YES')
        else:
            print('NO')