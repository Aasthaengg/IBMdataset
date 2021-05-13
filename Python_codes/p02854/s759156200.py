N = int(input())
A = [int(a) for a in input().split()]

cum_A = [A[0]] * N
for i in range(1, N):
    cum_A[i] = cum_A[i - 1] + A[i]

cost = None
for i in range(N):
    left = cum_A[i]
    right = cum_A[-1] - cum_A[i]
    if cost is None:
        cost = abs(left - right)
    else:
        cost = min(abs(left - right), cost)

print(cost)