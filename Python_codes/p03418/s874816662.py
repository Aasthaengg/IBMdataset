N, K = map(int, input().split())

ans = 0

if K == 0:
    print(N*N)
    exit()

for b in range(K+1, N+1):
    max_p = N // b
    max_q = N % b
    if max_q < K:
        max_p -= 1
        max_q = b - 1
    # print(b,max_p,max_q)
    ans += max_p * (b-K) + (max_q-K+1)

print(ans)
