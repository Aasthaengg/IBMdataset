n = int(input())
b = list(map(int, input().split()))
a = [0] * n

a[0] = b[0]
a[1] = b[0]
for i in range(1, n - 1):
    if b[i] < a[i]:
        a[i] = b[i]
    a[i +1] = b[i]
print(sum(a))