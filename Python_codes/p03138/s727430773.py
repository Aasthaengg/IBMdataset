N, K = map(int, input().split())
A = tuple(map(int, input().split()))
X = 0
for i in range(len(bin(K)) - 2, -1, -1):
    if (X + (1 << i)) > K:
        continue
    if sum((a >> i) & 1 for a in A) * 2 < N:
        X += (1 << i)
print(sum(a ^ X for a in A))
