N, M = map(int, input().split())
LL = 0
RR = N
for i in range(M):
    L, R = map(int, input().split())
    if LL < L:
        LL = L
    if RR > R:
        RR = R
print(max(0, RR - LL + 1))
