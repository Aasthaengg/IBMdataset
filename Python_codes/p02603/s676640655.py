N = int(input())
A = list(map(int, input().split()))

money = 1000
for i in range(N - 1):
    if A[i] < A[i+1]:
        num = money // A[i]
        profit = num * (A[i+1] - A[i])
        money += profit
print(money)
