N, M = map(int, input().split())

n = M
# 約数列挙(1,N)も含まれる
prime, i = set(), 1
while i * i <= n:
    if n % i == 0:
        prime.add(i)
        prime.add(n//i)
    i += 1

ans = 1
l = list(prime)
for i in l:
    if i * N <= M:
        ans = max(ans, i)

print(ans)
