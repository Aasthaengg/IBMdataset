def yakusu(n):
    results = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            results.append(i)
            results.append(n // i)
    return results

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in yakusu(sum(A)):
    M = sorted(map(lambda x: [x % i, (i-x % i)%i], A), key=lambda x: x[0])
    s = sum(map(lambda x: x[1], M))
    sm = 0
    for j, (m, m2) in enumerate(M):
        sm += m
        s -= m2
        if sm == s and s <=K:
            ans = max(ans, i)
print(ans)