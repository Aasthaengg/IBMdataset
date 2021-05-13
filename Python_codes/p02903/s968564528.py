import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W, A, B = mapint()
for i in range(1, H+1):
    if i<=B:
        print(''.join((['1']*A+['0']*(W-A))))
    else:
        print(''.join(['0']*A+['1']*(W-A)))