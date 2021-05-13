n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

cost = []
value = []
for i in range(n):
    if v[i] / c[i] > 1:
        cost.append(c[i])
        value.append(v[i])

print(sum(value) - sum(cost))
