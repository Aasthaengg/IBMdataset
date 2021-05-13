N, X, T = map(int, input().split())

x = int(N / X)

x = x + 1 if N % X != 0 else x

ans = T * x

print(ans)