n = int(input())
s = input()
best_cost = s.count('.')
cost = best_cost
for i in range(n):
  if s[i] == '#':
    cost += 1
  else:
    cost -= 1
  if cost < best_cost:
    best_cost = cost

print(best_cost)