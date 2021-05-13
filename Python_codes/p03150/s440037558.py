S = input()
l = len(S)
out = l - 7
ans = 'NO'
for i in range(7):
    s = S[:i] + S[i+out:]
    if s == 'keyence':
        ans = 'YES'
print(ans)