H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            cnt = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    tmp_i = i+di
                    tmp_j = j+dj
                    if (0 <= tmp_i <= H-1) and (0 <= tmp_j <= W-1) and (S[tmp_i][tmp_j]=="#"):
                        cnt += 1
            S[i][j] = cnt

for s in S:
    for i in s:
        print(i, end="")
    print()