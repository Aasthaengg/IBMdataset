W, a, b = map(int, input().split())
if a > b:
    a, b = b, a

ans = max(0, b - (a + W))
print(ans)
