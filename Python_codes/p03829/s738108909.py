n, a, b = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    if (x[i+1] - x[i]) * a >= b:
        ans += b
    else:
        ans += (x[i+1]-x[i]) * a
print(ans)