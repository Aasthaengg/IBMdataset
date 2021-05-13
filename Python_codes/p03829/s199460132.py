n, a, b = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    a_cost = (l[i + 1] - l[i]) * a
    if a_cost <= b:
        ans += a_cost
    else:
        ans += b
print(ans)