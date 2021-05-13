n = int(input())
a = [int(input()) for _ in range(n)]
b = a[:]
first = max(a)
idx = b.index(first)
b[idx] = 0
second = max(b)

for i in range(n):
    if a[i] == first:
        print(second)
    else:
        print(first)
