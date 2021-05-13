N = int(input())
ans = 0.0
for _ in range(N):
    xs, u = input().split()
    x = float(xs)
    if u == "JPY":
        ans += x
    else:
        ans += x * 380000.0
print(ans)