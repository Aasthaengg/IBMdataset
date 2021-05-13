n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)][::-1]

ans = 0
for a, b in ab:
    a += ans
    ans += -(-a//b)*b - a
print(ans)