#! python3
#  solve_119_B.py

N = int(input())
money = 0

for i in range(N):
    value,money_type = map(str,input().split())
    if money_type == "JPY":
        money += int(value)
    elif money_type == "BTC":
        money += float(value) * 380000
        
print(money)