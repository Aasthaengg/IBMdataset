total_stay = int(input())
normal_stay = int(input())
normal_cost = int(input())
discounted_cost = int(input())
if total_stay <= normal_stay:
  total_cost = total_stay * normal_cost
else:
  total_cost = normal_stay * normal_cost + (total_stay - normal_stay) * discounted_cost
print(total_cost)