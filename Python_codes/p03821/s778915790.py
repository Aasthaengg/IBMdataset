n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

count = 0
for i in reversed(range(n)):
    c = b[i] * (-(-a[i] // b[i])) - a[i]
    #for j in range(i):
    #    a[j] += c
    count += c
    if i >= 1:
        a[i-1] += count
print(count)
