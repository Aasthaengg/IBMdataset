N, K = map(int, input().split())
A = list(map(int, input().split()))

ans1 = 0
ans2 = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] < A[j]:
            ans2 += 1
        elif A[i] > A[j]:
            ans1 += 1

ans = ans1*(K*(K+1))//2 + ans2 * (K*(K-1))//2
ans = ans % (10**9+7)

print(ans)
