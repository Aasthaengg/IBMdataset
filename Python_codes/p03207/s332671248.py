n = int(input())
p = [int(input()) for _ in range(n)]

ans = sum(p)
ans -= max(p) // 2

print(ans)
