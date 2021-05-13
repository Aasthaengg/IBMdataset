N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N-K):
    a1 = A[i]
    a2 = A[i+K]
    if a1 < a2:
        ans.append('Yes')
    else:
        ans.append('No')

print(*ans, sep='\n')