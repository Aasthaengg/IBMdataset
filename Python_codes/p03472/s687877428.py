import math
N,H = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
amax = 0
ind = -1
for i in range(N):
    a,_ = X[i]
    if a>amax:
        amax = a
        ind = i
B = []
for i in range(N):
    _,b = X[i]
    if b>=amax:
        B.append(b)
B = sorted(B,reverse=True)
if sum(B)>=H:
    cnt = 0
    for i in range(len(B)):
        cnt += B[i]
        if cnt>=H:
            print(i+1)
            break
else:
    H -= sum(B)
    cnt = len(B)
    n = math.ceil(H/amax)
    print(cnt+n)