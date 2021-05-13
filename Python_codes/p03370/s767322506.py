donut_kind, ingredient = list(map(int, input().split(' ')))
need = [0]*donut_kind
for i in range(donut_kind):
  need[i] = int(input())
  
remain = ingredient - sum(need)
minimum = min(need)
mod = int(remain//minimum)
print(donut_kind + mod)