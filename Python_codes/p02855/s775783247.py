num = 0

def solve(cl, cr):
    P = []
    for i in range(cl, cr+1):
        for j in range(1, W+1):
            if S[i][j] == "#":
                P.append(j)
    P.sort()

    for i in range(len(P)):
        v1, v2 = 1, W
        if i >= 1:
            v1 = P[i-1] + 1
        if i < len(P) - 1:
            v2 = P[i]

        global num
        num += 1
        for j in range(cl, cr+1):
            for k in range(v1, v2+1):
                A[j][k] = num


H, W, K = map(int, input().split())
A = [[0 for _ in range(303)] for _ in range(303)]
S = [[" " for _ in range(303)] for _ in range(303)]
cnt = [0] * 303
for i in range(1, H+1):
    row = input()
    for j, c in enumerate(row, 1):
        if c == "#":
            cnt[i] += 1
        S[i][j] = c

vec = []
for i in range(1, H+1):
    if cnt[i] >= 1:
        vec.append(i)
for i in range(len(vec)):
    v1, v2 = 1, H
    if i >= 1:
        v1 = vec[i-1] + 1
    if i < len(vec) - 1:
        v2 = vec[i]

    solve(v1, v2)

for i in range(1, H+1):
    tmp = []
    for j in range(1, W+1):
        tmp.append(str(A[i][j]))
    print(" ".join(tmp))
