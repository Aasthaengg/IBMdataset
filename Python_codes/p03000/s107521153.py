import bisect
import sys
input = sys.stdin.readline

N,X = list(map(int,input().split()))
L = list(map(int,input().split()))
bn = [0]
for i in range(N):
    bn.append(bn[-1]+L[i])
print(bisect.bisect_right(bn,X))
