N = int(input())
A = list(map(int, input().split()))

stock = 0
money = 1000
for i in range(N-1):
    today = A[i]
    tomorrow = A[i+1]
    if today < tomorrow:
        # Buy
        n = money // today
        money -= n * today
        stock += n
    elif today > tomorrow:
        # Sell
        money += stock * today
        stock = 0
print(money + stock * A[-1])
