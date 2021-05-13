def sum_subarrays(A, mod=10**9+7):
    N = len(A)
    S = [0]
    for a in A:
        S.append(S[-1] + a)
        S[-1] %= mod
    return sum((2 * i - N) * s % mod for i, s in enumerate(S)) % mod

n,m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10 ** 9 + 7
diff_x = [x[i+1]-x[i] for i in range(n-1)]
diff_y = [y[i+1]-y[i] for i in range(m-1)]
ans = sum_subarrays(diff_x) * sum_subarrays(diff_y) % mod
print(ans)  