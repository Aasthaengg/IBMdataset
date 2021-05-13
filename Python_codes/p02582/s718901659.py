S = input()

tmp = 0
ans = 0
for i in range(len(S)):
    if S[i] == 'R':
        tmp += 1
        ans = max(ans, tmp)
    else:
        ans = max(ans, tmp)
        tmp = 0
print(ans) 