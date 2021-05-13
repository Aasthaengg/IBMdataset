N = int(input())
Menu = []
for _ in range(N):
    a, b = map(int, input().split())
    Menu.append((a + b, a, b))
Menu.sort(reverse=True)
ans = 0
for i, (_, a, b) in enumerate(Menu):
    if i % 2 == 0:
        ans += a
    else:
        ans -= b
print(ans)