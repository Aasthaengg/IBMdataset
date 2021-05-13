def digit_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    return res


N = int(input())
ans = N
for i in range(1, N):
    A = i
    B = N - i
    ans = min(ans, digit_sum(A) + digit_sum(B))
print(ans)
