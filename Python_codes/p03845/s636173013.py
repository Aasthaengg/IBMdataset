import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
M = int(input())
for i in range(M):
    P, X = map(int, input().split())
    TT = T.copy()
    TT[P-1] = X
    print(sum(TT))
