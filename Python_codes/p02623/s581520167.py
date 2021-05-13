N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
t = sum(B)
j = M
for i in range(N+1):
    while j > 0 and t > K:
        j -= 1
        t -= B[j]
    if t > K:
        break
    ans = max(ans, i+j)
    if i == N:
        break
    t += A[i]
print(ans)