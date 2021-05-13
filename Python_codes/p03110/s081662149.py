n = int(input())
ans = 0
for _ in range(n):
    x, u = input().split()
    c = 380000 if u == "BTC" else 1
    ans += float(x) * c
print(ans)