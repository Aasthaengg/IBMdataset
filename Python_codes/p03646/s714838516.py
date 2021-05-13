k = int(input())

n = 50
a = list(range(50))
base = k // n
r = k % n
for i in range(n):
    a[i] += base
for i in range(r):
    a[n-1-i] += 1
ans = a[n-r:] + a[:n-r]
print(n)
print(*ans)