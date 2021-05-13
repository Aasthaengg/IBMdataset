S = list(map(str, input().rstrip()))

ans = [0]*(len(S)+1)

for i, s in enumerate(S):
    if s=="<":
        ans[i+1] = max(ans[i+1], ans[i]+1)

ans = ans[::-1]
S = S[::-1]

for i, s in enumerate(S):
    if s==">":
        ans[i+1] = max(ans[i+1], ans[i]+1)

print(sum(ans))