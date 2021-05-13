n = int(input())
x_u = [input().split() for i in range(n)]

ans = 0
for x, u in x_u:
    if u == "JPY":
        ans += float(x)
    else:
        ans += float(x) * 380000.0
print(ans)