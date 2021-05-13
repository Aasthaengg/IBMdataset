N, K, S = map(int, input().split())
ans = [S for _ in range(K)]
dummy = S + 1 if S < 10 ** 9 else 1
for _ in range(N - K):
    ans.append(dummy)
print(*ans)
