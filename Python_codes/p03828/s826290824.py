#052_C
n = int(input())
mod = 10 ** 9 + 7

div = [0 for _ in range(n)]
for i in range(1, n+1):
    x = i
    for j in range(2, x+1):
        while x % j == 0:
            x //= j
            div[j-1] += 1
ans = 1
for i in range(n):
    ans = ans * (div[i] + 1) % mod

print(ans)