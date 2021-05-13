n = int(input())
ans = 0
for _ in range(n):
    x,v = input().split()
    if v == 'BTC':
        ans += float(x) * 380000
    else:
        ans += int(x)
print(ans)
