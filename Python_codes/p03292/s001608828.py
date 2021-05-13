A = sorted(list(map(int, input().split())), reverse=True)
cost = 0
for i in range(len(A) - 1):
    cost += (abs(A[i + 1] - A[i]))
print(cost)
