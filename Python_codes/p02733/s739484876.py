from itertools import product
H,W,K = map(int,input().split())
S = [input().strip() for _ in range(H)]
C = {i:[0 for _ in range(W+1)] for i in range(H)}
for i in range(H):
    for j in range(1,W+1):
        C[i][j] = C[i][j-1]+int(S[i][j-1])
cmin = (H-1)*(W-1)
for x in product((0,1),repeat=H-1):
    A = []
    cur = 0
    for i in range(H-1):
        if x[i]==1:
            A.append(list(range(cur,i+1)))
            cur = i+1
    A.append(list(range(cur,H)))
#     print("A={}".format(A))
    cur = 0
    cnt = 0
    ind = 0
    for j in range(1,W+1):
        flag = 0
        for a in A:
            tot = 0
            for i in a:
                tot += C[i][j]-C[i][cur]
            if tot<=K:continue
            else:
                flag = 1
                break
        if flag==1:
            cnt += 1
            if cur==j-1:
                ind = 1
                break
            cur = j-1
    if ind==0:
        cmin = min(cmin,cnt+sum(x))
#     print("cmin={},x={}".format(cmin,x))
print(cmin)               