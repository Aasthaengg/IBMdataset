W, a, b = map(int, input().split())

if a + W < b:
    ans = b - (a + W)
elif a <=  b <= b + W or a <= b + W <= a + W:
    ans = 0
elif b + W < a:
    ans = a - (b+W)

print(ans)