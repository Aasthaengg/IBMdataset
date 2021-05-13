n = int(input())
ab = [list(map(int, input().split())) for i in range(n)][::-1]

ans = 0
for a, b in ab:
    a += ans
    # 負の剰余。
    ans += -a % b
print(ans)