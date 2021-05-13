S = input()

flg = False
Z = [0,0]
N = len(S)
ans = [0] * N
for i, s in enumerate(S):
    if (flg and s == "R"):
        flg = False
        if tmp_R%2 == 0:
            ans[tmp_R] = Z[0]
            ans[tmp_L] = Z[1]
        else:
            ans[tmp_R] = Z[1]
            ans[tmp_L] = Z[0]
        Z = [0, 0]

    if (not flg) and s == "L":
        flg = True
        tmp_R = i-1
        tmp_L = i

    if i%2 == 0:
        Z[0] += 1
    else:
        Z[1] += 1

    if i == N-1:
        if tmp_R%2 == 0:
            ans[tmp_R] = Z[0]
            ans[tmp_L] = Z[1]
        else:
            ans[tmp_R] = Z[1]
            ans[tmp_L] = Z[0]

print(*ans)
