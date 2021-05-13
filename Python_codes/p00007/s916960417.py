n=int(input())
debt=100
adds=1.05
for i in range(n):
    debt*=adds
    if debt%1!=0:
        debt=int(debt)+1
print(debt*1000)