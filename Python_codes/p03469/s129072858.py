S = input()
ans = ''
for i in range(len(S)):
    if i == 3:
        ans += '8'
    else:
        ans += S[i]
print(ans)