H, W, *SS = open(0).read().split()
H, W = int(H), int(W)

R = [[0]*(W) for _ in [0]*(H)]
C = [[0]*(W) for _ in [0]*(H)]

for i, S in enumerate(SS):
    cnt = 0
    pre = S[0]
    for j, s in enumerate(S):
        if s == '.':
            cnt += 1
        else:
            if pre == '.':
                for k in range(1, cnt+1):
                    R[i][j-k] = cnt
                cnt = 0
        pre = s
    if pre == '.':
        for k in range(1, cnt+1):
            R[i][-k] = cnt

for j in range(W):
    cnt = 0
    pre = SS[0][j]
    for i in range(H):
        s = SS[i][j]
        if s == '.':
            cnt += 1
        else:
            if pre == '.':
                for k in range(1, cnt+1):
                    C[i-k][j] = cnt
                cnt = 0
        pre = s
    if pre == '.':
        for k in range(1, cnt+1):
            C[-k][j] = cnt

ans = 0
for i in range(H):
    for j in range(W):
        if R[i][j] and C[i][j]:
            area = R[i][j]+C[i][j]-1
            if ans < area:
                ans = area
print(ans)