N,M,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_accumulate_cost = [0]
lastCost = 0
for i in range(N):
    lastCost += A[i]
    A_accumulate_cost.append(lastCost)

B_accumulate_cost = [0]
lastCost = 0
for i in range(M):
    lastCost += B[i]
    B_accumulate_cost.append(lastCost)

max_num = 0
p = M
for i in range(N+1):
    A_cost = A_accumulate_cost[i]
    if A_cost > K:
        break

    for j in range(p, -1, -1):
        if A_cost + B_accumulate_cost[j] <= K:
            p = j
            if i + j > max_num:
                max_num = i+j
            break

print(max_num)