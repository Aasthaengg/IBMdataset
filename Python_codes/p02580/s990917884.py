import sys

H, W, M = map(int,input().split())
R = [0] * H
C = [0] * W

S = set()

for _ in range(M):
    h, w = map(int,input().split())
    S.add((h-1, w-1))
    R[h-1] += 1
    C[w-1] += 1

r = max(R)
c = max(C)

HL = [i for i in range(H) if R[i] == r]
WL = [i for i in range(W) if C[i] == c]

for h in HL:
    for w in WL:
        if not (h, w) in S:
            print(r + c)
            sys.exit()

print(r + c - 1)