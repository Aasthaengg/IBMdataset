N, L = map(int, input().split())
ans = 0
min = L

for i in range(1, N+1):
    a = L+i-1
    ans += a
    if abs(a) < abs(min):
        min = a

ans -= min
print(ans)