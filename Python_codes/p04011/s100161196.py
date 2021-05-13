stay = int(input())
days = int(input())
charge1 = int(input())
charge2 = int(input())
charge_total = 0

for i in range(stay):
    temp = i + 1
    if temp <= days:
        charge_total += charge1
    else:
        charge_total += charge2
print(charge_total)