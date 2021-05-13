N, K = map(int, input().split(" "))
mod = 10 ** 9 + 7
A = list(map(int, input().split(" ")))
num = [0 for i in range(N)]

trip = 0
for i in range(N):
    for j in range(N):
        if A[i] < A[j]:
            num[j] += 1
        if i < j and A[i] > A[j]:
            trip += 1

ans = (trip * K) % mod
for n in num:
    ans += n * K * (K - 1) // 2
    ans %= mod
print(ans)