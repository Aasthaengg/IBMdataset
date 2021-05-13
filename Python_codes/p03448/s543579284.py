*coins, X = [int(input()) for _ in range(4)]

price = [500, 100, 50]
payable = []

for a in range(coins[0]+1):
    for b in range(coins[1]+1):
        for c in range(coins[2]+1):
            payable.append(a*price[0] + b*price[1] + c*price[2])
            
print(payable.count(X))