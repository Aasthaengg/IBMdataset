N, X = map(int, input().split())
m = [int(input()) for i in range(N)]
m = sorted(m)

ans = N
X -= sum(m)
ans += X // m[0]

print(ans)
