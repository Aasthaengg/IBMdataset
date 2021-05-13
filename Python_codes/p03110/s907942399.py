from decimal import Decimal
N = int(input())
A = [list(input().split()) for _ in range(N)]
ans = 0
for x,u in A:
    if u == 'JPY':
        ans += int(x)
    else:
        ans += float(x)*380000
print(ans)