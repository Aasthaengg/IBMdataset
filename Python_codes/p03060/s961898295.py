n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(n):
    profit = v[i] - c[i]
    if 0 < profit:
        ans += profit
    else:
        continue

print(ans)