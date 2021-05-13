N = int(input())
S = list(input())
L = 0
R = S.count('E')
ans = L + R
for i in range(0, N):
    if S[i] == 'E':
        R -= 1
        R = max(0, R)
        ans = min(ans, L+R)
    else:
        L += 1
print(ans)