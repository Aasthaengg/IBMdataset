import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()

if B<A:
    print(0)
elif A!=B and N==1:
    print(0)
elif N<=2:
    print(1)
else:
    MIN = A*(N-1)+B
    MAX = B*(N-1)+A
    print(MAX-MIN+1)