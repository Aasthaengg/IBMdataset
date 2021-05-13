def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    table = list(table)
    return table


N = int(input())
A = list(map(int, input().split()))
temp = [0] * N
for n in reversed(range(1,N+1)):
    if (A[n-1] + temp[n - 1])%2 == 0:
        temp[n - 1] = 0
        continue
    for a in divisors(n):
        temp[a-1] += 1


res = list(i+1 for i, _ in enumerate(temp) if temp[i])
print(len(res))
print(*res)

"""
4
1 1 1 1
"""