S = list(input())

ans = "No"

if len(set(S)) == 2:
    if S.count(S[0]) == 2:
        ans = "Yes"

print(ans)