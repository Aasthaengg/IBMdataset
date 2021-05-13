n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(k):
    l = [0] * (n + 1)
    for j in range(n):
        l[max(0, j - a[j])] += 1
        l[min(n, j + a[j] + 1)] -= 1
    for j in range(n - 1):
        l[j + 1] += l[j]
    a = l
    if a.count(n) == n:
        break
print(*a[:n])