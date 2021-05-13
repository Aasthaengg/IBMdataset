debt = 100000
for i in range(int(input())):
    debt *= 1.05
    if debt % 1000 > 0:
        debt = int(debt/1000)*1000+1000
print(debt)