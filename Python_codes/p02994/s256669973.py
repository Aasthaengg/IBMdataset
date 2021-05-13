N, L = map(int, input().split())
a = [L+i for i in range(N)]
b = [abs(i) for i in a]

ans = 0
min_abs = max(b)
min_i = 0

for i in range(N):
    ans += a[i]
    if min_abs > b[i]:
        min_abs = b[i]
        min_i = i

ans -= a[min_i]
print(ans)
