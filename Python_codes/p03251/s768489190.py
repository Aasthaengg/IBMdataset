n, m, x_capital, y_capital = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = "War"

for i in range(100):
    if x_capital < i and i <= y_capital and max(x) < i and i <= min(y):
        ans = "No War"

print(ans)
