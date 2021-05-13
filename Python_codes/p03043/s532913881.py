a = [int(s) for s in input().split()]
N, K = a[0], a[1]
prob = 0
if N > K - 1: prob += (N - K + 1)/N
prob2 = 0
for i in range(1, min(N, K - 1) + 1):
    a = i
    j = 0
    while(a < K): 
        a = a << 1
        j += 1
    prob2 += 1/(2**j)
print(prob + prob2 * (1/N))
