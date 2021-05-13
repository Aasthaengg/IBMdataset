N, K, S = map(int, input().split())
U = str(S + 1) if S != 10 ** 9 else "1"
S = str(S)
ans = [S if i <= K - 1 else U for i in range(N)]
print(" ".join(ans))