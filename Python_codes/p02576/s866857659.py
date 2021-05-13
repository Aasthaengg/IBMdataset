
N,X,T = map(int, input().split())

ans = int(N / X) * T
ans += T if N % X != 0 else 0

print(ans)
