n = int(input())
S = input()
cW = S.count('.')
cB = 0
ans = cW
for i in range(n):
    if S[i]=='#':
        cB += 1
    else:
        cW -= 1
    ans = min(ans, cW+cB)
print(ans)