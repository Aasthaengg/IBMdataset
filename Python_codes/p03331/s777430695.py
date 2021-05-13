def digits_sum(n):
    return sum(int(c) for c in str(n))


N = int(input())
ans = float("inf")
for i in range(1, N):
    A = i
    B = N - i
    ans = min(ans, digits_sum(A) + digits_sum(B))
print(ans)
