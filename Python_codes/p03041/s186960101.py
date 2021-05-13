N, K = map(int, input().split())
S = str(input())
ans = ''
for i in range(N):
    if i == K-1:
        temp = S[i].lower()
        ans += temp
    else:
        ans += S[i]

print(ans)