N,M = map(int, input().split())
LR = list()
al = 0
ar = 0
for i in range(M):
    LR.append( list(map(int,input().split())) )
    L = LR[i][0]
    R = LR[i][1]
    if i == 0:
        al = L
        ar = R
    if al < L:
        al = L
    if ar > R:
        ar = R
    if ar < L or al > R:
        print(0)
        exit()
print(ar-al+1)