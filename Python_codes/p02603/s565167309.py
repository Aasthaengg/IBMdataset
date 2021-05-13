N = int(input())
*A, = map(int, input().split())

money = 1000
num_stock = 0
for a, b in zip(A, A[1:]):
    if a < b:
        cnt, money = divmod(money, a)
        num_stock += cnt
    elif a > b:
        money += num_stock * a
        num_stock = 0
money += num_stock * A[-1]
print(money)
