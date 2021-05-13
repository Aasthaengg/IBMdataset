X = int(input())

money = 100
year = 0
while money < X:
    year += 1
    money = str(money*101)
    money = int(money[:-2])
    
print(year)
