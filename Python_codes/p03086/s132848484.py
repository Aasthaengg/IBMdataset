s = input()
l = len(s)
ans = 0
for i in range(l):
    for j in range(l+1):
        for ss in s[i:j]:
            if ss not in 'ACGT':
                break
        else:
            ans = max(ans, len(s[i:j]))
print(ans)
