N, K = map(int, input().split())
count = 0
for i in range(1, N+1):
    if i < K:
        continue
    # print(i, (N // i)*(i-K), (N%i+1)-K)
    if K == 0:
        count += (N // i)*(i-K) + max(0, (N%i)-K)
    else:
        count += (N // i) * (i - K) + max(0, (N % i + 1) - K)
print(count)