N, K = map(int, input().split())
A = list(map(int, input().split()))

tab = [] * 64
X_tmp = 1
for i in range(64):
    tab_tmp = 0
    for j, Aj in enumerate(A):
        tab_tmp += ((Aj >> i) & 0b1)
    tab.append(tab_tmp)

X_ans = 0
for i_inv in range(64):
    i = 63 - i_inv
    if X_ans + (1 << i) > K: continue
    elif tab[i] * 2 >= N: continue
    else:
        X_ans += (1 << i)

# print("#", X_ans)

ans = 0
for Ai in A:
    ans += (Ai ^ X_ans)
print(ans)