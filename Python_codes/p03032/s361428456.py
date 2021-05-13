N, K = map(int, input().split())
V = list(map(int, input().split()))
Ans = -float('inf')
for a in range(K+1):
    for b in range(K+1):
        if a + b > min(K, N):
            break
        c = K - a - b
        A = V[:a] + V[N - b:]
        A.sort()
        ans = sum(A)
        for x in A:
            if c == 0:
                break
            if x >= 0:
                break
            if x < 0:
                c -= 1
                ans -= x
        Ans = max(ans, Ans)
print(Ans)



