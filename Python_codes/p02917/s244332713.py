n = int(input())
b = list(map(int, input().split()))
a = [0] * n

a[0] = b[0]
a[n - 1] = b[n - 2]
for i in range(n - 2):
    if b[i + 1] >= b[i]:
        a[i + 1] = b[i]
    else:
        a[i + 1] = b[i + 1]

print(sum(a))