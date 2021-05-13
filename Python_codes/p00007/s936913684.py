import math as m
yen = 100000
for i in range(int(input())):
    yen = m.ceil((yen*1.05)/1000)*1000
print(yen)