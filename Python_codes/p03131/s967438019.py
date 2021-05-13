k, a, b = map(int, input().split())
ans = k + 1
if a < b:
    k -= a - 1
    ans = max(ans, a + (b-a)*(k//2) + k%2)
print(ans)