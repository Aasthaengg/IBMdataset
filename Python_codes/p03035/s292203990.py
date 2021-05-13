a, b = map(int, input().split())

ans = b

if 12 >= a >= 6:
    ans = b // 2
if a <= 5:
    ans = 0

print(ans)
