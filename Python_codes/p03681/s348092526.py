def factrial(n):
    INF = 10 ** 9 + 7
    ret = 1
    for i in range(2, n + 1):  ret = (ret * i) % INF
    return ret

N, M = list(map(int,input().split()))
if abs(N - M) >= 2:  ans = 0
elif N == M:  ans = (2 * (factrial(N) ** 2)) % (10 ** 9 + 7)
else:  ans = factrial(N) * factrial(M)
print(ans % (10 ** 9 + 7))