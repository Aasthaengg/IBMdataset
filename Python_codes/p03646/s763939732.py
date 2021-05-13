k = int(input())
n = 50
a = [49 + k // n] * n
for i in range(k - k // n * n):
    a[i] += n + 1
    for j in range(n):
        a[j] -= 1
print(n)
print(' '.join(map(str, a)))