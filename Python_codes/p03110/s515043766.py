n = int(input())

rate = 380000.0
ans = 0.0
for i in range(n):
    x, u = input().split()
    x = float(x)
    ans += x * rate if u == 'BTC' else x
print(ans)   