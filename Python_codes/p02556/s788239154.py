n = int(input())
ans = 0
ma1, mi1 = -10000000000, 10000000000
ma2, mi2 = -10000000000, 10000000000
for i in range(n):
    x, y = map(int, input().split())
    ma1 = max(ma1, x - y)
    mi1 = min(mi1, x - y)
    ma2 = max(ma2, x + y)
    mi2 = min(mi2, x + y)
    ans = max(ans, ma1 - mi1, ma2 - mi2)
print(ans)