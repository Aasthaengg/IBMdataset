#! python3
#  solve127A.py

age,cost = map(int,input().split())

if age <= 5:
    cost = 0
elif 6 <= age <= 12:
    cost = cost//2
elif 7 <= age:
    cost = cost

print(cost)