from itertools import permutations
from collections import Counter
N=int(input())
XY=[list(map(int,input().split())) for _ in range(N)]
if N==1:print(1);exit()
a=[((A[0]-B[0]),(A[1]-B[1])) for A,B in permutations(XY,2)]
cnt = Counter(a)
print(N-cnt.most_common()[0][1])