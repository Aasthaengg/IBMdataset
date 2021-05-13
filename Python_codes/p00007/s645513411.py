from math import ceil 
def interest(debt, rate, weeks):
    if weeks == 1:
        return ceil(debt * (1 + rate))
    else:
        return ceil(interest(debt, rate, weeks - 1) * (1 + rate))

rounds = 1000
rate = 0.05
debt = 100000
weeks = int(input())
print(int(rounds*interest(debt/rounds, rate, weeks)))