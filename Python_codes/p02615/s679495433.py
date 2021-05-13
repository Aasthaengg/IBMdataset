n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
b = [a[0]]
for i in range(1, n):
    b.append(a[i])
    b.append(a[i])
print(sum(b[:n - 1]))
