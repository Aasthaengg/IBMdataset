s = input()
ans = [0]*(len(s)+1)
for i, c in enumerate(s):
    if c=='<':
        ans[i+1] = max(ans[i+1], ans[i]+1)
for i, c in enumerate(s[::-1]):
    if c=='>':
        ans[-2-i] = max(ans[-2-i], ans[-1-i]+1)
print(sum(ans))