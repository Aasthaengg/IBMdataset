H,W,N = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
C = {}
for i in range(N):
    a,b = X[i]
    if a-2>=1 and b-2>=1:
        if (a-2,b-2) not in C:
            C[(a-2,b-2)] = 0
        C[(a-2,b-2)] += 1
    if a-2>=1 and b-1>=1 and b+1<=W:
        if (a-2,b-1) not in C:
            C[(a-2,b-1)] = 0
        C[(a-2,b-1)] += 1
    if a-2>=1 and b+2<=W:
        if (a-2,b) not in C:
            C[(a-2,b)] = 0
        C[(a-2,b)] += 1
    if a-1>=1 and b-2>=1 and a+1<=H:
        if (a-1,b-2) not in C:
            C[(a-1,b-2)] = 0
        C[(a-1,b-2)] += 1
    if a-1>=1 and b-1>=1 and a+1<=H and b+1<=W:
        if (a-1,b-1) not in C:
            C[(a-1,b-1)] = 0
        C[(a-1,b-1)] += 1
    if a-1>=1 and a+1<=H and b+2<=W:
        if (a-1,b) not in C:
            C[(a-1,b)] = 0
        C[(a-1,b)] += 1
    if b-2>=1 and a+2<=H:
        if (a,b-2) not in C:
             C[(a,b-2)] = 0
        C[(a,b-2)] += 1
    if b-1>=1 and a+2<=H and b+1<=W:
        if (a,b-1) not in C:
            C[(a,b-1)] = 0
        C[(a,b-1)] += 1
    if a+2<=H and b+2<=W:
        if (a,b) not in C:
            C[(a,b)] = 0
        C[(a,b)] += 1
D = {i:0 for i in range(10)}
for c in C:
    D[C[c]] += 1
cnt = 0
for i in range(1,10):
    cnt += D[i]
D[0] = (H-2)*(W-2)-cnt
for i in range(10):
    print(D[i])