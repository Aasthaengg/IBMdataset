n = int(input())
a = list(input().split())
b = []
a = a[::-1]
for i in range(n)[::2]:
    b.append(a[i])
a = a[::-1]
if n % 2 != 0:
    a.pop(0)
for i in range(len(a))[::2]:
    b.append(a[i])
print(' '.join(b))