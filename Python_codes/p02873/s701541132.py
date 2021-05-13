S = input()
N = len(S) + 1

l = [0] * N
r = [0] * N

tmp_l = 0
# <,>,>の場合、l=[0,1,0,0]となる
for i in range(N - 1):
    if S[i] == "<":

        tmp_l += 1
        l[i + 1] = tmp_l
    else:
        tmp_l = 0

tmp_r = 0
# Sを逆からチェック
#<,>,>の場合、l=[0,2,1,0]となる
for i in range(N - 2, -1, -1):
    if S[i] == ">":
        tmp_r += 1
        r[i] = tmp_r
    else:
        tmp_r = 0

ans = 0
for i in range(N):
    ans += max(l[i], r[i])

print(ans)
