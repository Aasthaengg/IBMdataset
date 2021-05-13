import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = [True if int(input())%2==0 else False for _ in range(N)]

if all(As):
    print('second')
else:
    print('first')
