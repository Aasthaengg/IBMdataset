n, k = map(int, input().split())
a = [int(i) for i in input().split()]
for j in range(min(k, 42)):
    bit = [0 for _ in range(n)]
    for i in range(n):
        bit[max(i - a[i], 0)] += 1
        if i + a[i] + 1 < n:
            bit[i + a[i] + 1] -= 1
    result = [bit[0]]
    for i in range(n - 1):
        result.append(bit[i + 1] + result[-1])
    a = result
print(' '.join(list(map(str, a))))
