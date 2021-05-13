S = input()

ans = 0

for l in range(len(S)):
    for r in range(l, len(S)):
        T = S[l:r+1]
        if set(T) <= set('ACGT'):
            ans = max(ans, r-l+1)

print(ans)