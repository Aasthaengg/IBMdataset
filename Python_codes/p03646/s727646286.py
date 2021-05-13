k = int(input())

n = 50

p = k // n
q = k % n

a = [i+p for i in range(n-1, -1, -1)]

if q > 0:
    for i in range(q):
        a[i] += 1

print(n)
print(*a)