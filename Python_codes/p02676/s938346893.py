K = int(input())
S = input()

S_len = len(S)
ans = ""

if S_len > K:
    ans += S[0:K]+"..."
else:
    ans += S
print(ans)
