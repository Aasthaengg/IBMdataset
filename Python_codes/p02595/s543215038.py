#下手にlist作って呼び出すよりも、逐次計算するほうが早い？
n, d = map(int, input().split())
ans = 0
d = d ** 2

for i in range(n):
    x, y = map(int, input().split())
    if d >= x ** 2 + y ** 2:
        ans += 1

print(ans)