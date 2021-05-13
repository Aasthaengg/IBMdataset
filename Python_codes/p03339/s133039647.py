N = int(input())
S = input()

cum_e_cnt = [0]*(N)
for i in range(0, N):
    if i==0:
        if S[0] == "E":
            cum_e_cnt[0] = 1
    if S[i] == "E":
        cum_e_cnt[i] = cum_e_cnt[i-1] + 1
    else:
        cum_e_cnt[i] = cum_e_cnt[i-1]

cum_w_cnt = [0]*(N)
for i in range(0, N):
    if i==0:
        if S[0] == "W":
            cum_w_cnt[0] = 1
    if S[i] == "W":
        cum_w_cnt[i] = cum_w_cnt[i-1] + 1
    else:
        cum_w_cnt[i] = cum_w_cnt[i-1]

#l==0
ans = cum_e_cnt[N-1] - cum_e_cnt[0]
for l in range(1, N):
    ans = min(ans, cum_w_cnt[l-1] + cum_e_cnt[N-1] - cum_e_cnt[l])
print(ans)
