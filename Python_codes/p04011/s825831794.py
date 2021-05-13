stay = int(input())
change_day = int(input())
first_cost = int(input())
change_cost = int(input())
total_cost = 0
 
for i in range(stay):
 if(i < change_day):
  total_cost += first_cost
 else:
  total_cost += change_cost
print(total_cost)