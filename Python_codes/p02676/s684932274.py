K=int(input())
S=str(input())
if len(S) <= K:
    print(S)
else:
    ans = S[0]
    for i in range(1,K):
        ans += S[i]
    ans += "..."
    print(ans)
