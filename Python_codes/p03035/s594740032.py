age,yen = map(int,input().split())

cost = 0

if age >= 13:
    cost = yen
elif age >= 6 and age <= 12:
    cost = yen/2

elif age <= 5:
    cost = 0

print(int(cost))