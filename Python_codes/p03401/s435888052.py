n = int(input())
A = list(map(int, input().split()))
plan = [0] + A + [0]
cost = sum([abs(plan[i] - plan[i - 1]) for i in range(1, len(plan))])

for i in range(1, n + 1):
    diff = (abs(plan[i - 1] - plan[i]) + abs(plan[i] - plan[i + 1])) - abs(plan[i - 1] - plan[i + 1])
    print(cost - diff)