def split_sum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


N = int(input())
ans = float('inf')
for A in range(1, N):
    B = N - A
    if A > B:
        break
    ans = min(ans, split_sum(A) + split_sum(B))
print(ans)
