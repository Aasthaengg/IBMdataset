N, M, K = map(int, input().split())
if K % N == 0 or K % M == 0:
    print('Yes')
    exit()
candidates = set()
for i in range(1, N):
    curr = i * M
    for j in range(1, M):
        curr += N - 2 * i
        candidates.add(curr)
print('Yes') if K in candidates else print('No')
