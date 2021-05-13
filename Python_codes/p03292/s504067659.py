def actual(a1, a2, a3):
    A = sorted([a1, a2, a3])

    amount_cost = 0
    
    for i in range(len(A) - 1):
        amount_cost += A[i + 1] - A[i]

    return amount_cost

a1, a2, a3 = map(int, input().split())
print(actual(a1, a2, a3))