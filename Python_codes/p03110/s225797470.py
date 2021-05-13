n = int(input())
ans = 0
for _ in range(n):
    a,b = map(str,input().split())
    if b == 'BTC':
        ans += float(a) * 380000
    else:
        ans += int(a)
print(ans)
