#%%
s = 'CODEFESTIVAL2016'
s = list(s)
n = list(input())
ans = 0
for i in range(len(s)):
    if s[i] != n[i]:
        ans += 1
print(ans)

