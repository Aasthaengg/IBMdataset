N, K = map(int, input().split())
A = list(map(int, input().split()))


ones = [0] * (len(bin(K)) - 2)
for a in A:
    for i in range(len(ones)):
        if (1 << i) & a:
            ones[i] += 1

best_bits = [1 if x * 2 < N else 0 for x in ones]
best_k = sum(2 ** i * b for i, b in enumerate(best_bits))
if K < best_k:
    better = 0
    for i in range(len(ones) - 1, -1, -1):
        if best_bits[i]:
            b = 1 << i
            if better + b <= K:
                better += b
    best_k = better

answer = 0
for a in A:
    answer += a ^ best_k
print(answer)