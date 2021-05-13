per_cost, possess, times = map(int, input().split())

MAX_cost = times * per_cost

if (possess >= MAX_cost):
    ans = times
else:
    ans = possess // per_cost

print(ans)
