n, x = (int(x) for x in input().split())
M = [int(input()) for _ in range(n)]
x -= sum(M)
ans = n + x // min(M)
print(ans)
