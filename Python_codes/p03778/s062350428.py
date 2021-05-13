W, a, b = map(int, input().split())
if a < a + W <= b:
    ans = b - (a + W)
elif a <= b <= a + W:
    ans = 0
elif a <= b + W <= a + W:
    ans = 0
else:
    ans = a - (b + W)
print(ans)
