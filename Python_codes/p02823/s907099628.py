import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()
if abs(A-B)%2==0:
    print(abs(A-B)//2)
else:
    if A>B:
        A, B, = B, A
    c = A + (B-A-1)//2
    d = (N-B+1) + (B-A-1)//2
    print(min(c, d))