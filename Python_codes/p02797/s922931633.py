N, K, S = map(int, input().split())

if S == 10**9:
    ans = ' '.join([str(S) for _ in range(K)]+[str(1) for _ in range(N-K)])
else:
    ans = ' '.join([str(S) for _ in range(K)]+[str(S+1) for _ in range(N-K)])

print(ans)