N, K, S = map(int, input().split())
ans = []
for _ in range(K):
    ans.append(S)
for _ in range(N - K):
    if S == 10 ** 9:
        ans.append(1)
    else:
        ans.append(S + 1)
print(" ".join(map(str, ans)))