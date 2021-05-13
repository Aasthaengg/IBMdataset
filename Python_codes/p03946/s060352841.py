N, T = map(int, input().split())
A = list(map(int, input().split()))

min_A = 10**10
max_A = 0
profit = []
for i in range(N):
    if A[i] <= min_A:
        profit.append(max_A - min_A)
        min_A = A[i]
        max_A = A[i]
    elif A[i] >= max_A:
        profit.append(max_A - min_A)
        max_A = A[i]
profit.append(max_A - min_A)        
        
max_profit = max(profit)
count = 0
for i in range(len(profit)):
    if profit[i] == max_profit:
        count += 1
        
print(count)