inp=input()
list =inp.split()
age, cost=list[0], list[1]
age=int(age)
cost=int(cost)
if age>=13:
  cost=cost
elif age<13 and age>5:
  cost=cost*0.5
else:
  cost=0
print(int(cost))