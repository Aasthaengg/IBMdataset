import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = []
Bs = []
for _ in range(N):
    A, B = mapint()
    As.append(A)
    Bs.append(B)
As.sort()
Bs.sort()

if N%2==1:
    left = As[N//2]
    right = Bs[N//2]
else:
    left = (As[N//2]+As[N//2-1])
    right = (Bs[N//2]+Bs[N//2-1])

print(right-left+1)