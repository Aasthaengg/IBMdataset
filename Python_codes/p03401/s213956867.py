n = int(input())
al = list(map(int, input().split()))
al = [0] + al + [0]
costs = []

for i in range(n+1):
    costs.append(abs(al[i+1] - al[i]))

d = sum(costs)

for i in range(1, n+1):
    distance = d - abs(al[i] - al[i+1]) - abs(al[i-1] - al[i]) + abs(al[i-1] - al[i+1])
    print(distance)
