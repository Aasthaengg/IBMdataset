per_cost, possess, times = map(int, input().split())

ans = min(possess // per_cost, times)
print(ans)