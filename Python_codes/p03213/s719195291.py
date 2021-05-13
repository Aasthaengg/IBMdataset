def f(n):
    return len(list(filter(lambda x: x >= n - 1, l)))
n = int(input())
l = [0] * (n + 1)
for i in range(2, n+1):
    cur = i
    for j in range(2, i+1):
        while cur % j == 0:
            l[j] += 1
            cur //= j
print(f(75) + f(25) * (f(3) - 1) + f(15) * (f(5) - 1) + f(5) * (f(5) - 1) * (f(3) - 2) // 2)