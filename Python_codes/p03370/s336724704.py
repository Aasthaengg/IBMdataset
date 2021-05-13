N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
X -= sum(m[:N])
ans = N
ans += X // min(m)
print(ans)