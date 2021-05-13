n = int(input())
a = [x for x in input().split()]
b = []

if n % 2 == 1:
    for i in reversed(range(1, n+1, 2)):
        b.append(a[i-1])
    for i in range(2, n, 2):
        b.append(a[i-1])
else:
    for i in reversed(range(2, n+1, 2)):
        b.append(a[i-1])
    for i in range(1, n, 2):
        b.append(a[i-1])
    
print(*b, sep=' ')
