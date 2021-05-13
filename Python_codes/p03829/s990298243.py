n, a, b = map(int,input().split())
x = list(map(int,input().split()))

cost = 0
for i in range(1, n):
    ca = a * (x[i] - x[i-1])
    cost += min(ca, b)
print(cost)