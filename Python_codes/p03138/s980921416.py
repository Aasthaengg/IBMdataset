N, K = map(int, input().split())
A = list(map(int, input().split()))
ans, k = 0, 0
for i in range(40)[::-1]:
    b = 1 << i
    c = sum(bool(a & b) for a in A)
    if k + b <= K and c < N - c:
        k += b
        ans += b * (N - c)
    else:
        ans +=  b * c
print(ans)