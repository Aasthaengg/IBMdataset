from itertools import accumulate

N,M,K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

accA = list(accumulate(A))
accB = list(accumulate(B))

maxbook = 0
idx_B = M
for idx_A in range(N+1):
    time = accA[idx_A]
    for j in range(idx_B, -1, -1):
        if time + accB[j] <= K:
            idx_B = j
            break
    if time + accB[idx_B] <= K:
        maxbook = max(maxbook, idx_A + idx_B)

print(maxbook)