N = int(input())
S = input()

ans = 0

for i in range(N):
    tmp = len(set(S[:i]) & set(S[i:]))
    ans = max(ans, tmp)

print(ans)