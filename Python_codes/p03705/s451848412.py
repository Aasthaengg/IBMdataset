n, a, b = map(int, input().split())
ran = b - a

if ran < 0:
    ans = 0
elif ran == 0:
    ans = 1
elif n == 1:
    ans = 0
else:
    ans = (b - a)*(n - 2) + 1
print(ans)
