k = int(input())

n = 50

q, r = divmod(k, n)
ans = [n - 1 - k + q * (n + 1)] * n
for i in range(r):
    ans[i] += n + 1

print(n)
print(*ans)
