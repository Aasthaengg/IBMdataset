N, M = map(int, input().split())

prime, i = set(), 1
while i * i <= M:
    if M % i == 0:
        prime.add(i)
        prime.add(M//i)
    i += 1

ans = 0
for i in prime:
    if i * N <= M:
        ans = max(ans, i)
print(ans)
