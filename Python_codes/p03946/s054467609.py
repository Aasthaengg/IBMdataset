N, T = map(int, input().split())
A = list(map(int, input().split()))

right = [0] * (N+1)
for i in range(N-1,-1,-1):
    right[i+1] = max(right[i], A[i])
left = [10 ** 9 + 7] * (N+1)
for i in range(N):
    left[i+1] = min(left[i], A[i])

profit = 0
cnt = 0
for i in range(1,N+1):
    if profit == right[i]-left[i]:
        cnt += 1
    elif profit < right[i]-left[i]:
        cnt = 1
        profit = right[i]-left[i]

print(cnt)

