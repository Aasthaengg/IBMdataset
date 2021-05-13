N, K = map(int, input().split())
S = input()

ans = ""
for i, s in enumerate(S):
    if i == K-1:
        ans += s.lower()
    else:
        ans += s
print(ans)
