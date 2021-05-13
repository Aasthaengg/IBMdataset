s = input().strip()
N=len(s)
ans=0
for i in range(N):
    for j in range(i, N):
        if all('ACGT'.count(c) == 1 for c in s[i : j + 1]):
            ans = max(ans, j - i + 1)
print(ans)