n = int(input())

a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(a[i] - i - 1)

b.sort()
median = b[n // 2]

c = []
for i in range(n):
    c.append(abs(b[i] - median))

print(sum(c))
