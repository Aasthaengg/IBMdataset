N, M, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(M):
    if X < A[i]:
        ans = i
        break
print(min(ans, M-ans))