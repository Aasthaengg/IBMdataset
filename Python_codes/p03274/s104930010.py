N, K = list(map(int,input().split()))
A = list(map(int,input().split()))
ans = 10 ** 9 + 7
for i in range(N - K + 1):
    left = A[i]
    right = A[i + K - 1]
    if right < 0:  temp = -left
    elif left >= 0:  temp = right
    else:  temp = right - left + min(-left, right)
    ans = min(ans, temp)
print(ans)