MOD = 10 ** 9 + 7
import math


def compute_reverse(n: list):
    result = 0
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] > n[j]:
                result += 1
    return result


N, K = map(int, input().split())
A = list(map(int, input().split()))
case1 = compute_reverse(A) *  ((K * (K + 1)) // 2)
case3 = compute_reverse(A[::-1]) * ((K * (K - 1)) // 2)
ans = (case1 + case3) % MOD
print(ans)