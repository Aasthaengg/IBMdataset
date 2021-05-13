N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

ans = len(m)
X = X - sum(m)

ans += X // min(m)
print(ans)
