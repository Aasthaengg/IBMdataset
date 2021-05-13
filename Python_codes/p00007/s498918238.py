import math

def Interest(money,n):
    for i in range(n):
        money *= 1.05
        money = math.ceil(money)
    return money

m = 100
n = int(input())

print int(Interest(m,n)*1000)