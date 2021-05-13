S = input()
ans = 0
for k in range(1,len(S)):
    if S[k-1] != S[k]:
        ans += 1
print(ans)
