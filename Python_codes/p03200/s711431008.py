S = input()
N = len(S)
W_cnt = 0
ans = 0
for i in range(N):
    if S[i] == "W":
        ans += i - W_cnt
        W_cnt += 1
print(ans)
