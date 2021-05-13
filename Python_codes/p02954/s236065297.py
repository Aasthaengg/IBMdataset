# AtCoder
S = input()
N = len(S)

ans = [1]*N
ans_n = len(ans)

for i in range(N-2):
    if S[i:i+2] == "RR":
        ans[i+2] += ans[i]
        ans[i] = 0

for i in range(ans_n-1, 1, -1):
    if S[i-1:i+1] == "LL":
        ans[i-2] += ans[i]
        ans[i] = 0

print(" ".join(map(str, ans)))
