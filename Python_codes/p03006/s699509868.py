from collections import Counter
N=int(input())
XY=[tuple(map(int, input().split())) for _ in range(N)]
PQ=[(x1-x2,y1-y2) for x1,y1 in XY for x2,y2 in XY if x1!=x2 or y1!=y2]
C=Counter(PQ)
print(N-C.most_common(1)[0][1] if N!=1 else 1)