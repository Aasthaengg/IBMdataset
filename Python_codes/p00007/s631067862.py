debt = 100000
n = int(input())
for i in range(n):
    debt *= 1.05
    if debt%1000 != 0:
        debt = (debt//1000+1)*1000 

print(int(debt))