N = int(input())
*A, = map(int, input().split())

dp1 = [A[0]]
dp2 = [-A[0]]
for i in range(1, N-1):
    dp1.append(max(dp1[i-1] + A[i], dp2[i-1] - A[i]))
    dp2.append(max(dp1[i-1] - A[i], dp2[i-1] + A[i]))
dp1.append(dp1[-1] + A[N-1])
dp2.append(dp2[-1] - A[N-1])


print(max(dp1[-1], dp2[-1]))