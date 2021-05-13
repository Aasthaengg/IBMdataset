N, K = map(int, input().split())
S = input()

tmp = S[0]
S_lst = []
if S[0] == '0':
    S_lst.append(0)  # 逆立ちから始める

ct = 0
for s in S:
    if tmp == s:
        ct += 1
    else:
        S_lst.append(ct)
        tmp = s
        ct = 1
if ct:
    S_lst.append(ct)

if S[-1] == '0':
    S_lst.append(0)  # 逆立ちで終える

l, r = 0, K * 2

M = sum(S_lst[:K * 2 + 1])
ans = M
while r < len(S_lst) - 2:
    M += S_lst[r + 1] + S_lst[r + 2] - S_lst[l] - S_lst[l + 1]
    ans = max(ans, M)
    l += 2
    r += 2
print(ans)
