n = int(input())
ans = 0
def g(n):
    return n * (n + 1) // 2

for num in range(1, n+1):
    ans += g(n // num) * num
print(ans)