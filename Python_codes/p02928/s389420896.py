from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
A_sort0 = sorted(A)
A_sort = sorted(list(set(A)))
counter = Counter(A)
ans = 0
for i in range(len(A_sort)):
    if i == 0:
        continue
    else:
        q = A_sort0.index(A_sort[i])
        ans += (q * (K * (K-1) // 2) * counter[A_sort[i]])  % MOD
        index = A.index(A_sort[i])
        cnt = 0
        p = 0
        for j in range(index, N):
            if A_sort[i] > A[j]:
                cnt += 1 * p
            elif A_sort[i] == A[j]:
                p += 1
        ans = (ans + (cnt * K)) % MOD
print(ans)
