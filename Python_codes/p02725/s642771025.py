k, n = map(int, input().split())
a = list(map(int, input().split()))

last = a[0] + k - a[n - 1]
sum = 0
l =[]

for i in range(1, n):
    l.append(a[i] - a[i - 1])

l.append(last)

print(k - max(l))
