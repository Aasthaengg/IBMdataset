S = input()
T = input()
lens = len(S)
lent = len(T)

ans = -1
for i in range(lens-lent+1):
    S2 = S[i:i+lent]
    diff = 0
    for j in range(lent):
        if S2[j] != T[j]:
            diff += 1
    if ans == -1:
        ans = diff
    else:
        if ans > diff:
            ans = diff
print(ans)