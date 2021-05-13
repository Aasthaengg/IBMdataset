n = int(input())
b = [10**6] + list(map(int, input().split()))
a = [0] * n
a[0] = b[1]
a[n-1] = b[n-1]

for i in range(1, n-1):
    a[i] = min(b[i], b[i+1])

print(sum(a))
