
X =int(input())
Now_Rate = 100
Counter = 0
while Now_Rate < X:
    Now_Rate += Now_Rate//100
    Counter += 1
print(Counter)
