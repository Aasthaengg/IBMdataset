n = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0

for i in range(1, n):
    if A[i-1] > A[i]:
        money += stock * A[i-1]
        stock = 0
    else:
        stock += money // A[i-1]
        money %= A[i-1]
else:
    money += stock * A[-1]
    stock = 0

print(money)
