n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    value = 0
    cost = 0
    for j in range(n):
        if ((i >> j) & 1):
            value += v[j]
            cost += c[j]
        ans = max(ans, value - cost)

print(ans)
