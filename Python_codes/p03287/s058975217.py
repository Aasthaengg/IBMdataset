N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
S = [0]
for i in range(N):
    S.append(A[i])
    S[i + 1] += S[i]

counter = {}
ans = 0
for r in range(1, N + 1):
    if (S[r - 1] % M) in counter:
        counter[S[r - 1] % M] += 1
    else:
        counter[S[r - 1] % M] = 1

    if (S[r] % M) in counter:
        ans += counter[S[r] % M]

print(ans)