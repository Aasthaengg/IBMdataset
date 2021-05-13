import math
def DebtHell():
    n = int(input())
    debt = 100000
    
    while n>0:
        n-=1
        debt*=1.05
        debt = int(int(math.ceil(debt/1000)*1000))

    print(debt)
    
    
DebtHell()