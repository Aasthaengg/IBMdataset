A = list(map(int, input().split()))

orders = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
ans = []

for order in orders:
    cost = abs(A[order[0]] - A[order[1]]) + abs(A[order[1]] - A[order[2]])
    ans.append(cost)
    
print(min(ans))