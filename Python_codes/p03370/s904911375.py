n, x = map(int, input().split())
M = [int(input()) for i in range(n)]

ans = n
x -= sum(M)
ans += x // min(M)

print(ans)