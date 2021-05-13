N = int(input())

ans = 0
for _ in range(N):
    x, u = input().split()
    x = float(x)
    ans += x if u == 'JPY' else x * 380000
print(ans)
